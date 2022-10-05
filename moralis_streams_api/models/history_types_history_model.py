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

class HistoryTypesHistoryModel(object):
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
        'id': 'str',
        '_date': 'str',
        'payload': 'WebhookTypesIWebhook',
        'error_message': 'str',
        'webhook_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_date': 'date',
        'payload': 'payload',
        'error_message': 'errorMessage',
        'webhook_url': 'webhookUrl'
    }

    def __init__(self, id=None, _date=None, payload=None, error_message=None, webhook_url=None):  # noqa: E501
        """HistoryTypesHistoryModel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__date = None
        self._payload = None
        self._error_message = None
        self._webhook_url = None
        self.discriminator = None
        self.id = id
        self._date = _date
        self.payload = payload
        self.error_message = error_message
        self.webhook_url = webhook_url

    @property
    def id(self):
        """Gets the id of this HistoryTypesHistoryModel.  # noqa: E501


        :return: The id of this HistoryTypesHistoryModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HistoryTypesHistoryModel.


        :param id: The id of this HistoryTypesHistoryModel.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this HistoryTypesHistoryModel.  # noqa: E501


        :return: The _date of this HistoryTypesHistoryModel.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this HistoryTypesHistoryModel.


        :param _date: The _date of this HistoryTypesHistoryModel.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def payload(self):
        """Gets the payload of this HistoryTypesHistoryModel.  # noqa: E501


        :return: The payload of this HistoryTypesHistoryModel.  # noqa: E501
        :rtype: WebhookTypesIWebhook
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this HistoryTypesHistoryModel.


        :param payload: The payload of this HistoryTypesHistoryModel.  # noqa: E501
        :type: WebhookTypesIWebhook
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def error_message(self):
        """Gets the error_message of this HistoryTypesHistoryModel.  # noqa: E501


        :return: The error_message of this HistoryTypesHistoryModel.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this HistoryTypesHistoryModel.


        :param error_message: The error_message of this HistoryTypesHistoryModel.  # noqa: E501
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

        self._error_message = error_message

    @property
    def webhook_url(self):
        """Gets the webhook_url of this HistoryTypesHistoryModel.  # noqa: E501


        :return: The webhook_url of this HistoryTypesHistoryModel.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this HistoryTypesHistoryModel.


        :param webhook_url: The webhook_url of this HistoryTypesHistoryModel.  # noqa: E501
        :type: str
        """
        if webhook_url is None:
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501

        self._webhook_url = webhook_url

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
        if issubclass(HistoryTypesHistoryModel, dict):
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
        if not isinstance(other, HistoryTypesHistoryModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
