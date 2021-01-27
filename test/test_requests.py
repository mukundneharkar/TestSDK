import logging
import random
import sys
import threading
import time

sys.path.append("..")
from lmingest.api.lm_response_interface import LMResonseInterface

import lmingest
from lmingest.api.lm_metrics import MetricsApi
from lmingest.models.lm_datapoint import LMDataPoint
from lmingest.models.lm_datasource import LMDataSource
from lmingest.models.lm_datasource_instance import LMDataSourceInstance
from lmingest.models.lm_resource import LMResource

max_host = 1
max_ds = 1
max_inst = 2
max_dp = 5
max_values = 5

# logger = logging.getLogger('lmingest.api')
# logger.setLevel(logging.DEBUG)
logging.basicConfig()
logger = logging.getLogger('lmingest.api')


def random_string(max):
  return "_" + str(random.randint(1, max))


def random_object(type):
  if type == 'resource':
    name = "MukundSdk" + random_string(max_host)
    return LMResource(ids={"system.hostname": name},
                      create=True, name=name, properties={'mukund.sdk': 'true'})
  if type == 'datasource':
    return LMDataSource(name="Mukundds" + random_string(max_ds))
  if type == 'instance':
    return LMDataSourceInstance(name="instance" + random_string(max_inst))
  if type == 'datapoint':
    return LMDataPoint(name="dp1" + random_string(max_dp))
  if type == 'values':
    values = {}
    t = int(time.time())
    for i in range(random.randint(1, max_values)):
      values[t] = random.randint(0, 100)
      t = t - 1
    return values


configuration = lmingest.Configuration(company='qauat', authentication={
  'id': '6zCEvh43taGMFP42SSmF',
  'key': 'Q)bdX2q7u[G79gfz5^P8{HT)g-uq[5+E9SS%Mb{^'})

'''
configuration.company = 'qauat'
configuration.access_id = '6zCEvh43taGMFP42SSmF'
configuration.access_key = 'Q)bdX2q7u[G79gfz5^P8{HT)g-uq[5+E9SS%Mb{^'
configuration.logger_format = '%(asctime)s  %(levelname)s  %(message)s'

configuration.company = 'qapr'
configuration.access_id = '59M55J26848bQxvEy8th'
configuration.access_key = 'DzUByF6V33L=2Y-Wb8S675ZxzV6kE33g5c[KP+[F'
configuration.access_id = 'vZAYN697FQ8I9WY35BQL'
configuration.access_key = 'k(K6iuy(y%N923)38G]Tdu%xz]3Jn(2uEG[c+52i'
'''
authentication = {'id': 'vZAYN697FQ8I9WY35BQL',
                  'key': 'k(K6iuy(y%N923)38G]Tdu%xz]3Jn(2uEG[c+52i'}
company = 'lmmukundneharkar'

'''
authentication = {'id':
                    'Gzp4muArPszz9M69r9x4',
                  'key': '8=9+}g{9j5EA5)2%R_xD37Z-(M{a^h7)QrBNPAqz'}
company = 'lmdhirashah'
'''

configuration.authentication = authentication
configuration.company = company

configuration.logger['lmingest.api'] = logger
configuration.debug = False


# configuration.logger_file = None

class MyResponse(LMResonseInterface):

  def success_callback(self, request, response, status, request_id):
    print(response, status, request_id)

  def error_callback(self, request, response, status, reason, request_id):
    print(response, status, reason, request_id)


def producer():
  metric_api = MetricsApi(lmingest.ApiClient(configuration), interval=30,
                          response_callback=MyResponse(),
                          batch=True)
  while True:
    resource = random_object("resource")
    datasource = random_object("datasource")
    instance = random_object("instance")
    datapoint = random_object("datapoint")
    m = metric_api.SendMetrics(resource=resource,
                               datasource=datasource,
                               instance=instance,
                               datapoint=datapoint,
                               values=random_object("values"))
    # logger.info("response %s", m)
    # resource.name = "chanfging this later on"
    # logger.info("resource %s", resource)
    time.sleep(10)


def MetricRequest():
  t = threading.Thread(target=producer)
  t.daemon = True
  t.start()


MetricRequest()
# LogRequest()
time.sleep(50000000)
