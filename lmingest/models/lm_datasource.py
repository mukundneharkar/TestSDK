# coding: utf-8


import pprint
import re  # noqa: F401

import six

from lmingest.utils.object_name_validator import ObjectNameValidator

objectNameValidator = ObjectNameValidator()


class LMDataSource(object):
  """
  This model is used to defining the datasource object.

  Args:
      name (str): DataSource unique name. Used to match an existing DataSource.
        If no existing DataSource matches the name provided here, a new
        DataSource is created with this name.
      display_name (str):  DataSource display name. Only considered when creating a new DataSource.
      group (str): DataSource group name. Only considered when DataSource does
        not already belong to a group. Used to organize the DataSource within
        a DataSource group. If no existing DataSource group matches, a new
        group is created with this name and the DataSource is organized under
        the new group.
      id (int): DataSource unique ID. Used only to match an existing DataSource.
        If no existing DataSource matches the provided ID, an error results.

  """

  def __init__(self, name, display_name=None,
      group=None, id=None):  # noqa: E501

    self._name = None
    self._display_name = None
    self._group = None
    self._id = None
    self.discriminator = None

    if name is not None:
      self.name = name
    if display_name is not None:
      self.display_name = display_name
    if group is not None:
      self.group = group
    if id is not None:
      self.id = id
    error_msg = self._valid_field()
    if error_msg is not None and len(error_msg) > 0:
      raise ValueError(error_msg)

  def __hash__(self):
    return hash(str(self.name))

  @property
  def name(self):
    """DataSource unique name. Used to match an existing DataSource. If no
    existing DataSource matches the name provided here, a new DataSource is created with this name.

    :return: The data_source of this LMDataSource.
    :rtype: str
    """
    return self._name

  @name.setter
  def name(self, data_source):
    err_msg = objectNameValidator.check_datasource_name_validation(data_source)
    if err_msg:
      raise ValueError(err_msg)
    self._name = data_source

  @property
  def display_name(self):
    """DataSource display name. Only considered when creating a new DataSource.

    :return: The display_name of this LMDataSource.
    :rtype: str
    """
    return self._display_name

  @display_name.setter
  def display_name(self, display_name):
    err_msg = objectNameValidator.check_datasource_displayname_validation(
        display_name)
    if err_msg:
      raise ValueError(err_msg)
    self._display_name = display_name

  @property
  def group(self):
    """DataSource group name. Only considered when DataSource does not already
    belong to a group. Used to organize the DataSource within a DataSource
    group. If no existing DataSource group matches, a new group is created with
    this name and the DataSource is organized under the new group.

    :return: The group of this LMDataSource.
    :rtype: str
    """
    return self._group

  @group.setter
  def group(self, group):
    err_msg = objectNameValidator.check_datasource_group_validation(group)
    if err_msg:
      raise ValueError(err_msg)
    self._group = group

  @property
  def id(self):
    """DataSource unique ID. Used only to match an existing DataSource. If no
    existing DataSource matches the provided ID, an error results.

    :return: The id of this LMDataSource.  # noqa: E501
    :rtype: int
    """
    return self._id

  @id.setter
  def id(self, id):
    if id is not None and id != 0 and id < 0:
      raise ValueError("DataSource Id {%s} should not be negative." % id)
    self._id = id

  def to_dict(self):
    result = {}

    for attr, _ in six.iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(map(
            lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
            value
        ))
      elif hasattr(value, "to_dict"):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(map(
            lambda item: (item[0], item[1].to_dict())
            if hasattr(item[1], "to_dict") else item,
            value.items()
        ))
      else:
        if value != None:
          result[attr] = value
    if issubclass(LMDataSource, dict):
      for key, value in self.items():
        result[key] = value

    return result

  def to_str(self):
    return pprint.pformat(self.to_dict())

  def __repr__(self):
    """For `print` and `pprint`"""
    return self.to_str()

  def __eq__(self, other):
    """Returns true if both objects are equal"""
    if not isinstance(other, LMDataSource):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """Returns true if both objects are not equal"""
    return not self == other

  def _valid_field(self):
    data_source_id = self.id
    err_msg = ""
    if data_source_id == 0:
      # dataSource Validations
      err_msg += objectNameValidator.check_datasource_name_validation(self.name)

      # dataSourceDisplayName Validations
      err_msg += objectNameValidator.check_datasource_displayname_validation(
          self.display_name)

      # dataSourceGroup validations
      err_msg += objectNameValidator.check_datasource_group_validation(
          self.group)

    elif data_source_id != 0:
      if data_source_id < 0:
        err_msg += "DataSource Id {%s} should not be negative." % data_source_id

      # dataSource Validations
      err_msg += objectNameValidator.check_datasource_name_validation(self.name)

      # dataSourceDisplayName Validations
      err_msg += objectNameValidator.check_datasource_displayname_validation(
          self.display_name)

      # dataSourceGroup validations
      err_msg += objectNameValidator.check_datasource_group_validation(
          self.group)

    return err_msg
