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

class Log(object):
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
        'tag': 'str',
        'stream_id': 'str',
        'stream_type': 'str',
        'log_index': 'str',
        'transaction_hash': 'str',
        'address': 'str',
        'data': 'str',
        'topic0': 'str',
        'topic1': 'str',
        'topic2': 'str',
        'topic3': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'stream_id': 'streamId',
        'stream_type': 'streamType',
        'log_index': 'logIndex',
        'transaction_hash': 'transactionHash',
        'address': 'address',
        'data': 'data',
        'topic0': 'topic0',
        'topic1': 'topic1',
        'topic2': 'topic2',
        'topic3': 'topic3'
    }

    def __init__(self, tag=None, stream_id=None, stream_type=None, log_index=None, transaction_hash=None, address=None, data=None, topic0=None, topic1=None, topic2=None, topic3=None):  # noqa: E501
        """Log - a model defined in Swagger"""  # noqa: E501
        self._tag = None
        self._stream_id = None
        self._stream_type = None
        self._log_index = None
        self._transaction_hash = None
        self._address = None
        self._data = None
        self._topic0 = None
        self._topic1 = None
        self._topic2 = None
        self._topic3 = None
        self.discriminator = None
        self.tag = tag
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.log_index = log_index
        self.transaction_hash = transaction_hash
        self.address = address
        self.data = data
        self.topic0 = topic0
        self.topic1 = topic1
        self.topic2 = topic2
        self.topic3 = topic3

    @property
    def tag(self):
        """Gets the tag of this Log.  # noqa: E501


        :return: The tag of this Log.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Log.


        :param tag: The tag of this Log.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def stream_id(self):
        """Gets the stream_id of this Log.  # noqa: E501


        :return: The stream_id of this Log.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this Log.


        :param stream_id: The stream_id of this Log.  # noqa: E501
        :type: str
        """
        if stream_id is None:
            raise ValueError("Invalid value for `stream_id`, must not be `None`")  # noqa: E501

        self._stream_id = stream_id

    @property
    def stream_type(self):
        """Gets the stream_type of this Log.  # noqa: E501


        :return: The stream_type of this Log.  # noqa: E501
        :rtype: str
        """
        return self._stream_type

    @stream_type.setter
    def stream_type(self, stream_type):
        """Sets the stream_type of this Log.


        :param stream_type: The stream_type of this Log.  # noqa: E501
        :type: str
        """
        if stream_type is None:
            raise ValueError("Invalid value for `stream_type`, must not be `None`")  # noqa: E501

        self._stream_type = stream_type

    @property
    def log_index(self):
        """Gets the log_index of this Log.  # noqa: E501


        :return: The log_index of this Log.  # noqa: E501
        :rtype: str
        """
        return self._log_index

    @log_index.setter
    def log_index(self, log_index):
        """Sets the log_index of this Log.


        :param log_index: The log_index of this Log.  # noqa: E501
        :type: str
        """
        if log_index is None:
            raise ValueError("Invalid value for `log_index`, must not be `None`")  # noqa: E501

        self._log_index = log_index

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this Log.  # noqa: E501


        :return: The transaction_hash of this Log.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this Log.


        :param transaction_hash: The transaction_hash of this Log.  # noqa: E501
        :type: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def address(self):
        """Gets the address of this Log.  # noqa: E501


        :return: The address of this Log.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Log.


        :param address: The address of this Log.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def data(self):
        """Gets the data of this Log.  # noqa: E501


        :return: The data of this Log.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Log.


        :param data: The data of this Log.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def topic0(self):
        """Gets the topic0 of this Log.  # noqa: E501


        :return: The topic0 of this Log.  # noqa: E501
        :rtype: str
        """
        return self._topic0

    @topic0.setter
    def topic0(self, topic0):
        """Sets the topic0 of this Log.


        :param topic0: The topic0 of this Log.  # noqa: E501
        :type: str
        """
        if topic0 is None:
            raise ValueError("Invalid value for `topic0`, must not be `None`")  # noqa: E501

        self._topic0 = topic0

    @property
    def topic1(self):
        """Gets the topic1 of this Log.  # noqa: E501


        :return: The topic1 of this Log.  # noqa: E501
        :rtype: str
        """
        return self._topic1

    @topic1.setter
    def topic1(self, topic1):
        """Sets the topic1 of this Log.


        :param topic1: The topic1 of this Log.  # noqa: E501
        :type: str
        """
        if topic1 is None:
            raise ValueError("Invalid value for `topic1`, must not be `None`")  # noqa: E501

        self._topic1 = topic1

    @property
    def topic2(self):
        """Gets the topic2 of this Log.  # noqa: E501


        :return: The topic2 of this Log.  # noqa: E501
        :rtype: str
        """
        return self._topic2

    @topic2.setter
    def topic2(self, topic2):
        """Sets the topic2 of this Log.


        :param topic2: The topic2 of this Log.  # noqa: E501
        :type: str
        """
        if topic2 is None:
            raise ValueError("Invalid value for `topic2`, must not be `None`")  # noqa: E501

        self._topic2 = topic2

    @property
    def topic3(self):
        """Gets the topic3 of this Log.  # noqa: E501


        :return: The topic3 of this Log.  # noqa: E501
        :rtype: str
        """
        return self._topic3

    @topic3.setter
    def topic3(self, topic3):
        """Sets the topic3 of this Log.


        :param topic3: The topic3 of this Log.  # noqa: E501
        :type: str
        """
        if topic3 is None:
            raise ValueError("Invalid value for `topic3`, must not be `None`")  # noqa: E501

        self._topic3 = topic3

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
        if issubclass(Log, dict):
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
        if not isinstance(other, Log):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
