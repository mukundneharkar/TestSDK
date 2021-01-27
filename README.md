# The LogicMonitor Python Ingestion library
This Python Library is suitable for ingesting the metrics, logs into the LogicMonitor Platform

## PushMetrics
### Overview 
LogicMonitor's Push Metrics feature allows you to send metrics directly to the LogicMonitor platform via a dedicated API, removing the need to route the data through a LogicMonitor Collector. Once ingested, these metrics are presented alongside all other metrics gathered via LogicMonitor, providing a single pane of glass for metric monitoring and alerting.

More details are available on [support site](https://www.logicmonitor.com/support)

## Version
- API version: 0.0.1
- Package version: 0.0.1

## Requirements.

Python 2.7 and 3.4+

## Installation

### pip install

If the python package ishosted on Github, you can install directly from Github

```sh
pip install git+ssh://git@stash.logicmonitor.com:7999/dev/lmingestpy.git
```

(you may need to run `pip` with root
permission: `sudo pip install git+ssh://git@stash.logicmonitor.com:7999/dev/lmingestpy.git`)

Then import the package:

```python
import lmingest 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import lmingest
```

## Getting Started

Please follow the [installation procedure](#Installation) and then run the following:

```python
from __future__ import print_function
import time
import random
import lmingest

from lmingest.api.lm_metrics import MetricsApi
from lmingest.models.lm_datapoint import LMDataPoint
from lmingest.models.lm_datasource import LMDataSource
from lmingest.models.lm_datasource_instance import LMDataSourceInstance
from lmingest.models.lm_resource import LMResource

# Configure API key authorization: LMv1
configuration = lmingest.Configuration(company = 'YOUR_COMPANY', authentication={ 'id': 'YOUR_ACCESS_ID', 'key' : 'YOUR_ACCESS_KEY'})

# create an instance of the API class
metric_api = MetricsApi(lmingest.ApiClient(configuration), interval=20, batch = True)
resource = LMResource(ids={"system.hostname": "SampleDevice"}, create=True, name="SampleDevice", properties={'some.sdk': 'true'})
ds = LMDataSource(name="DSName")
instance = LMDataSourceInstance(name="instance")
dp = LMDataPoint(name="dataPoint")

while True:
  values = { time.time() : random.randint() }
  metric_api.SendMetrics(resource=resource,
                       datasource=ds,
                       instance=instance,
                       datapoint=dp,
                       values=values)
  time.sleep(10)
```

## Documentation for API Endpoints

All URIs are relative to *https://<ACOUNT_NAME>.logicmonitor.com/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LMInstancePropertiesApi* | [**
instance_property_ingest_patch**](docs/LMInstancePropertiesApi.md#instance_property_ingest_patch) | **
PATCH** /instance_property/ingest | UpdateInstancePropertiesAPI
*LMInstancePropertiesApi* | [**
instance_property_ingest_put**](docs/LMInstancePropertiesApi.md#instance_property_ingest_put) | **
PUT** /instance_property/ingest | UpdateInstancePropertiesAPI
*LMMetricIngestApi* | [**metric_ingest_post**](docs/LMMetricIngestApi.md#metric_ingest_post) | **
POST** /metric/ingest | MetricIngestAPI
*LMResourcePropertiesApi* | [**
resource_property_ingest_patch**](docs/LMResourcePropertiesApi.md#resource_property_ingest_patch) | **
PATCH** /resource_property/ingest | UpdateResourcePropertiesAPI
*LMResourcePropertiesApi* | [**
resource_property_ingest_put**](docs/LMResourcePropertiesApi.md#resource_property_ingest_put) | **
PUT** /resource_property/ingest | UpdateResourcePropertiesAPI

## Documentation For Models

- [ListRestDataPointV1](docs/ListRestDataPointV1.md)
- [ListRestDataSourceInstanceV1](docs/ListRestDataSourceInstanceV1.md)
- [MapStringString](docs/MapStringString.md)
- [PushMetricAPIResponse](docs/PushMetricAPIResponse.md)
- [RestDataPointV1](docs/RestDataPointV1.md)
- [RestDataSourceInstanceV1](docs/RestDataSourceInstanceV1.md)
- [RestInstancePropertiesV1](docs/RestInstancePropertiesV1.md)
- [RestMetricsV1](docs/RestMetricsV1.md)
- [RestResourcePropertiesV1](docs/RestResourcePropertiesV1.md)

## Documentation For Authorization

## LMv1

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## Author

## TODO

- [X] Exception Handling, passing any error to end user when ever he makes a Send request for that
   resource. e.g. SendMetrics is invoked against the resources which are not present
- [X] Supporting the single request 
- [] Validation all the models. e.g. no specical chars allowed in the resource name, length
   restriction...etc
- [X] Property Updation API
- [] Send* call using the unique name
- [] Code commenting for code documentation
- [] Any other authentication support
- [] version/Compression support in send* call
- [] Test cases and sample program.


