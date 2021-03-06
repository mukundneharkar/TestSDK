# coding: utf-8

"""
    LogicMonitor API-Ingest Rest API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. API-Ingest provides the entry point in the form of public rest APIs for ingesting metrics into LogicMonitor. For using this application users have to create LMAuth token using access id and key from santaba.  # noqa: E501

    OpenAPI spec version: 3.0.0

"""

from __future__ import absolute_import

import logging
import re  # noqa: F401

import six

from lmingest import RestMetricsV1
from lmingest.api_client import ApiClient
from lmingest.internal.internal_cache import BatchingCache

# python 2 and python 3 compatibility library

logger = logging.getLogger('lmingest.api')


class LogsApi(BatchingCache):
  """NOTE: This class is auto generated by the swagger code generator program.

  Do not edit the class manually.
  Ref: https://github.com/swagger-api/swagger-codegen
  """
  """
  Attributes:
    swagger_types (dict): The key is attribute name
                          and the value is attribute type.
    attribute_map (dict): The key is attribute name
                          and the value is json key in definition.
  """
  swagger_types = {
    'api_client': 'ApiClient',
    'count': 'int',
    'interval': 'int',
    'size': 'int',
  }

  attribute_map = {
    'api_client': 'api_client',
    'count': 'count',
    'interval': 'interval',
    'size': 'size',
  }

  def __init__(self, api_client, interval=30, batch=True,
      response_callback=None):
    if api_client is None:
      api_client = ApiClient()
    self.api_client = api_client
    super(LogsApi, self).__init__(interval=interval, batch=batch,
                                  response_callback=response_callback,
                                  request_cb=self._do_request,
                                  merge_cb=self._merge_request)
    self._payload_cache = []

  def SendLogs(self, **kwargs):  # noqa: E501
    """LogIngestApi  # noqa: E501

    LogIngestApi is used for the purpose of ingesting raw metrics to the LM application. It needs metrics in the format of RestMetricsV1 object. Payload is then validated with series of validation, successfully verified metrics will be ingested to Kafka. Only POST method is applied to this API  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.log_ingest_post(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param bool create: Do you want to create resource? true/false
    :param RestMetricsV1 body:
    :return: PushMetricAPIResponse
             If the method is called asynchronously,
             returns the request thread.
    """

    all_params = ['resource', 'logs']  # noqa: E501
    params = locals()
    for key, val in six.iteritems(params['kwargs']):
      if key not in all_params:
        raise TypeError(
            "Got an unexpected keyword argument '%s' to method SendMetrics" % key
        )
      params[key] = val
    del params['kwargs']
    del params['self']
    del params['all_params']
    for one in all_params:
      if not params.__contains__(one):
        raise TypeError(
            "Some arguments are missing keys='%s'" %
            str(params.keys())
        )
    self.add_request(**kwargs)

  def _do_request(self):
    try:
      self.Lock()
      if len(self._payload_cache) > 0:
        self._counter.update({BatchingCache._PAYLOAD_TOTAL:
                                len(self._payload_cache)})
        response = self.log_ingest_post_with_http_info(
            body=self._payload_cache)
        logger.debug("Response is {}".format(response))
        self.response_handler(self._payload_cache, response[0], response[1],
                              response[2])
        self._payload_cache = []
        self._counter.update(BatchingCache._PAYLOAD_SEND)
      self._counter.update(BatchingCache._PAYLOAD_BUILD)
    except Exception as ex:
      logger.exception("Got Exception " + str(ex), exc_info=ex)
      self._counter.update(BatchingCache._PAYLOAD_EXCEPTION)
    finally:
      self.UnLock()

  def _merge_request(self, single_request):
    resource = single_request['resource']
    logs = single_request['logs']
    logs['_lm.resourceId'] = resource.ids
    self._payload_cache.append(logs)

  def log_ingest_post_with_http_info(self, **kwargs):  # noqa: E501
    """LogIngestApi  # noqa: E501

    LogIngestApi is used for the purpose of ingesting raw metrics to the LM application. It needs metrics in the format of RestMetricsV1 object. Payload is then validated with series of validation, successfully verified metrics will be ingested to Kafka. Only POST method is applied to this API  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.log_ingest_post_with_http_info(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param bool create: Do you want to create resource? true/false
    :param RestMetricsV1 body:
    :return: PushMetricAPIResponse
             If the method is called asynchronously,
             returns the request thread.
    """

    all_params = ['compression', 'body']  # noqa: E501
    all_params.append('async_req')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in six.iteritems(params['kwargs']):
      if key not in all_params:
        raise TypeError(
            "Got an unexpected keyword argument '%s'"
            " to method log_ingest_post" % key
        )
      params[key] = val
    del params['kwargs']

    collection_formats = {}
    path_params = {}
    query_params = []
    header_params = {}
    form_params = []
    local_var_files = {}

    body_params = None
    if 'body' in params:
      body_params = params['body']
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = self.api_client.select_header_content_type(
        # noqa: E501
        ['application/json'])  # noqa: E501

    # Authentication setting
    auth_settings = ['LMv1']  # noqa: E501
    # if the response type is a file, set _preload_content_value=false.
    # Because python 3.0+ 'utf-8' codec can't decode the binary string
    _response_type = None
    _preload_content_value = True
    if _response_type == 'file':
      _preload_content_value = False

    return self.api_client.call_api(
        '/log/ingest', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type=_response_type,
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', _preload_content_value),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)
