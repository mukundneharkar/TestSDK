import logging
import sys

sys.path.append("..")

import lmingest
from lmingest.api.lm_metrics import MetricsApi

logger = logging.getLogger('lmingest.api')
logger.setLevel(logging.DEBUG)

configuration = lmingest.Configuration(company='qauat', authentication={
  'id': '6zCEvh43taGMFP42SSmF',
  'key': 'Q)bdX2q7u[G79gfz5^P8{HT)g-uq[5+E9SS%Mb{^'}
                                       )

'''
configuration.company = 'qauat'
configuration.access_id = '6zCEvh43taGMFP42SSmF'
configuration.access_key = 'Q)bdX2q7u[G79gfz5^P8{HT)g-uq[5+E9SS%Mb{^'
configuration.logger_format = '%(asctime)s  %(levelname)s  %(message)s'

configuration.company = 'qapr'
configuration.access_id = '59M55J26848bQxvEy8th'
configuration.access_key = 'DzUByF6V33L=2Y-Wb8S675ZxzV6kE33g5c[KP+[F'
'''

configuration.logger['lmingest.api'] = logger
configuration.debug = False

metric_api = MetricsApi(lmingest.ApiClient(configuration), interval=5,
                        batch=True)
response = metric_api.UpdateResourceProperty(
    resourceIds={'system.deviceId': '233267'},
    resourceProperties={'put.asd': 'ksdasdd'},
    patch=False)
logger.info(response)

response = metric_api.UpdateInstanceProperty(
    resourceIds={'system.deviceId': '233267'}, dataSource='dsname_1',
    instanceName='instance_1', instanceProperties={
      'ins.asd': 'asad'},
)
logger.info(response)
