import logging
import random
import threading
import time

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

logger = logging.getLogger('lmingest.api')
logger.setLevel(logging.DEBUG)


def random_string(max):
  return "_" + str(random.randint(1, max))


def random_object(type):
  if type == 'resource':
    name = "MukundSdk" + random_string(max_host)
    return LMResource(ids={"system.hostname": name},
                      create=True, name=name, properties={'mukund.sdk': 'true'})
  if type == 'datasource':
    return LMDataSource(name="dsname" + random_string(max_ds))
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


configuration = lmingest.Configuration()
configuration.company = 'qauat'
configuration.access_id = '6zCEvh43taGMFP42SSmF'
configuration.access_key = 'Q)bdX2q7u[G79gfz5^P8{HT)g-uq[5+E9SS%Mb{^'
configuration.logger_format = '%(asctime)s  %(levelname)s  %(message)s'
configuration.logger['lmingest.api'] = logger
configuration.debug = True


# configuration.logger_file = None


def some_callback(request, response, status):
  logger.info("In Success_cb {%s}, {%s}, {%s}", request, response, status)


def producer():
  metric_api = MetricsApi(lmingest.ApiClient(configuration), interval=5,
                          success_cb=some_callback, error_cb=some_callback,
                          batch=False)
  try:
      while True:
        m = metric_api.SendMetrics(resource=random_object("resource"),
                                   datasource=random_object("datasource"),
                                   instance=random_object("instance"),
                                   datapoint=random_object("datapoint"),
                                   values=random_object("values"))
        logger.info("response %s", m)
        time.sleep(1)
  except ValueError as ex:
      logger.error("error: %s", ex)
  except Exception as ex:
      logger.error("error: %s", ex)



def MetricRequest():
  t = threading.Thread(target=producer)
  t.daemon = True
  t.start()


MetricRequest()
# LogRequest()
time.sleep(50000000)
