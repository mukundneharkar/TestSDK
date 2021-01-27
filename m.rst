The LogicMonitor Python Ingestion library
=========================================

This Python Library is suitable for ingesting the metrics, logs into the
LogicMonitor Platform

PushMetrics
-----------

Overview
~~~~~~~~

LogicMonitor’s Push Metrics feature allows you to send metrics directly
to the LogicMonitor platform via a dedicated API, removing the need to
route the data through a LogicMonitor Collector. Once ingested, these
metrics are presented alongside all other metrics gathered via
LogicMonitor, providing a single pane of glass for metric monitoring and
alerting.

More details are available on `support
site <https://www.logicmonitor.com/support>`__

Version
-------

-  API version: 0.0.1
-  Package version: 0.0.1

Requirements.
-------------

Python 2.7 and 3.4+

Installation
------------

pip install
~~~~~~~~~~~

If the python package ishosted on Github, you can install directly from
Github

.. code:: sh

   pip install git+ssh://git@stash.logicmonitor.com:7999/dev/lmingestpy.git

(you may need to run ``pip`` with root permission:
``sudo pip install git+ssh://git@stash.logicmonitor.com:7999/dev/lmingestpy.git``)

Then import the package:

.. code:: python

   import lmingest 

Setuptools
~~~~~~~~~~

Install via `Setuptools <http://pypi.python.org/pypi/setuptools>`__.

.. code:: sh

   python setup.py install --user

(or ``sudo python setup.py install`` to install the package for all
users)

Then import the package:

.. code:: python

   import lmingest

Getting Started
---------------

Please follow the `installation procedure <#Installation>`__ and then
run the following:

.. code:: python

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

Documentation for API Endpoints
-------------------------------

All URIs are relative to *https://.logicmonitor.com/rest*

+---------------+-----------------+-----------------+-----------------+
| Class         | Method          | HTTP request    | Description     |
+===============+=================+=================+=================+
| *LMInstanceP  | [*\*            |                 |                 |
| ropertiesApi* |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| instan        | \*\*            |                 |                 |
| ce_property_i |                 |                 |                 |
| ngest_patch** |                 |                 |                 |
| ](docs/LMInst |                 |                 |                 |
| ancePropertie |                 |                 |                 |
| sApi.md#insta |                 |                 |                 |
| nce_property_ |                 |                 |                 |
| ingest_patch) |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| PATCH*\*      | UpdateInstan    |                 |                 |
| /instance_pr  | cePropertiesAPI |                 |                 |
| operty/ingest |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| *LMInstanceP  | [*\*            |                 |                 |
| ropertiesApi* |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| in            | \*\*            |                 |                 |
| stance_proper |                 |                 |                 |
| ty_ingest_put |                 |                 |                 |
| **](docs/LMIn |                 |                 |                 |
| stancePropert |                 |                 |                 |
| iesApi.md#ins |                 |                 |                 |
| tance_propert |                 |                 |                 |
| y_ingest_put) |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| PUT*\*        | UpdateInstan    |                 |                 |
| /instance_pr  | cePropertiesAPI |                 |                 |
| operty/ingest |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| *LMMet        | `metric_i       | \*\*            |                 |
| ricIngestApi* | ngest_post <doc |                 |                 |
|               | s/LMMetricInges |                 |                 |
|               | tApi.md#metric_ |                 |                 |
|               | ingest_post>`__ |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| POST*\*       | MetricIngestAPI |                 |                 |
| /             |                 |                 |                 |
| metric/ingest |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| *LMResourceP  | [*\*            |                 |                 |
| ropertiesApi* |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| resour        | \*\*            |                 |                 |
| ce_property_i |                 |                 |                 |
| ngest_patch** |                 |                 |                 |
| ](docs/LMReso |                 |                 |                 |
| urcePropertie |                 |                 |                 |
| sApi.md#resou |                 |                 |                 |
| rce_property_ |                 |                 |                 |
| ingest_patch) |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| PATCH*\*      | UpdateResour    |                 |                 |
| /resource_pr  | cePropertiesAPI |                 |                 |
| operty/ingest |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| *LMResourceP  | [*\*            |                 |                 |
| ropertiesApi* |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| re            | \*\*            |                 |                 |
| source_proper |                 |                 |                 |
| ty_ingest_put |                 |                 |                 |
| **](docs/LMRe |                 |                 |                 |
| sourcePropert |                 |                 |                 |
| iesApi.md#res |                 |                 |                 |
| ource_propert |                 |                 |                 |
| y_ingest_put) |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+
| PUT*\*        | UpdateResour    |                 |                 |
| /resource_pr  | cePropertiesAPI |                 |                 |
| operty/ingest |                 |                 |                 |
+---------------+-----------------+-----------------+-----------------+

Documentation For Models
------------------------

-  `ListRestDataPointV1 <docs/ListRestDataPointV1.md>`__
-  `ListRestDataSourceInstanceV1 <docs/ListRestDataSourceInstanceV1.md>`__
-  `MapStringString <docs/MapStringString.md>`__
-  `PushMetricAPIResponse <docs/PushMetricAPIResponse.md>`__
-  `RestDataPointV1 <docs/RestDataPointV1.md>`__
-  `RestDataSourceInstanceV1 <docs/RestDataSourceInstanceV1.md>`__
-  `RestInstancePropertiesV1 <docs/RestInstancePropertiesV1.md>`__
-  `RestMetricsV1 <docs/RestMetricsV1.md>`__
-  `RestResourcePropertiesV1 <docs/RestResourcePropertiesV1.md>`__

Documentation For Authorization
-------------------------------

LMv1
----

-  **Type**: API key
-  **API key parameter name**: Authorization
-  **Location**: HTTP header

Author
------

TODO
----

-  ☒ Exception Handling, passing any error to end user when ever he
   makes a Send request for that resource. e.g. SendMetrics is invoked
   against the resources which are not present
-  ☒ Supporting the single request
-  [] Validation all the models. e.g. no specical chars allowed in the
   resource name, length restriction…etc
-  ☒ Property Updation API
-  [] Send\* call using the unique name
-  [] Code commenting for code documentation
-  [] Any other authentication support
-  [] version/Compression support in send\* call
-  [] Test cases and sample program.
