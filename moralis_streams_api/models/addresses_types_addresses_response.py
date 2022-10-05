# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddressesTypesAddressesResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'result': 'list[Addresses]',
        'cursor': 'str',
        'total': 'float'
    }

    attribute_map = {
        'result': 'result',
        'cursor': 'cursor',
        'total': 'total'
    }

    def __init__(self, result=None, cursor=None, total=None):  # noqa: E501
        """AddressesTypesAddressesResponse - a model defined in Swagger"""  # noqa: E501
        self._result = None
        self._cursor = None
        self._total = None
        self.discriminator = None
        self.result = result
        if cursor is not None:
            self.cursor = cursor
        self.total = total

    @property
    def result(self):
        """Gets the result of this AddressesTypesAddressesResponse.  # noqa: E501

        Array of project Streams  # noqa: E501

        :return: The result of this AddressesTypesAddressesResponse.  # noqa: E501
        :rtype: list[Addresses]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AddressesTypesAddressesResponse.

        Array of project Streams  # noqa: E501

        :param result: The result of this AddressesTypesAddressesResponse.  # noqa: E501
        :type: list[Addresses]
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def cursor(self):
        """Gets the cursor of this AddressesTypesAddressesResponse.  # noqa: E501

        Cursor for fetching next page  # noqa: E501

        :return: The cursor of this AddressesTypesAddressesResponse.  # noqa: E501
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """Sets the cursor of this AddressesTypesAddressesResponse.

        Cursor for fetching next page  # noqa: E501

        :param cursor: The cursor of this AddressesTypesAddressesResponse.  # noqa: E501
        :type: str
        """

        self._cursor = cursor

    @property
    def total(self):
        """Gets the total of this AddressesTypesAddressesResponse.  # noqa: E501

        Total count of streams on the project  # noqa: E501

        :return: The total of this AddressesTypesAddressesResponse.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this AddressesTypesAddressesResponse.

        Total count of streams on the project  # noqa: E501

        :param total: The total of this AddressesTypesAddressesResponse.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
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
                result[attr] = value
        if issubclass(AddressesTypesAddressesResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddressesTypesAddressesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other