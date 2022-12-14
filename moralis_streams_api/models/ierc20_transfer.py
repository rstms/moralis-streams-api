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

class IERC20Transfer(object):
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
        'transaction_hash': 'str',
        'contract': 'str',
        'log_index': 'str',
        'tag': 'str',
        '_from': 'str',
        'to': 'str',
        'value': 'str',
        'token_decimals': 'str',
        'token_name': 'str',
        'token_symbol': 'str',
        'value_with_decimals': 'str'
    }

    attribute_map = {
        'transaction_hash': 'transactionHash',
        'contract': 'contract',
        'log_index': 'logIndex',
        'tag': 'tag',
        '_from': 'from',
        'to': 'to',
        'value': 'value',
        'token_decimals': 'tokenDecimals',
        'token_name': 'tokenName',
        'token_symbol': 'tokenSymbol',
        'value_with_decimals': 'valueWithDecimals'
    }

    def __init__(self, transaction_hash=None, contract=None, log_index=None, tag=None, _from=None, to=None, value=None, token_decimals=None, token_name=None, token_symbol=None, value_with_decimals=None):  # noqa: E501
        """IERC20Transfer - a model defined in Swagger"""  # noqa: E501
        self._transaction_hash = None
        self._contract = None
        self._log_index = None
        self._tag = None
        self.__from = None
        self._to = None
        self._value = None
        self._token_decimals = None
        self._token_name = None
        self._token_symbol = None
        self._value_with_decimals = None
        self.discriminator = None
        self.transaction_hash = transaction_hash
        self.contract = contract
        self.log_index = log_index
        self.tag = tag
        self._from = _from
        self.to = to
        self.value = value
        self.token_decimals = token_decimals
        self.token_name = token_name
        self.token_symbol = token_symbol
        if value_with_decimals is not None:
            self.value_with_decimals = value_with_decimals

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this IERC20Transfer.  # noqa: E501


        :return: The transaction_hash of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this IERC20Transfer.


        :param transaction_hash: The transaction_hash of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def contract(self):
        """Gets the contract of this IERC20Transfer.  # noqa: E501


        :return: The contract of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this IERC20Transfer.


        :param contract: The contract of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if contract is None:
            raise ValueError("Invalid value for `contract`, must not be `None`")  # noqa: E501

        self._contract = contract

    @property
    def log_index(self):
        """Gets the log_index of this IERC20Transfer.  # noqa: E501


        :return: The log_index of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._log_index

    @log_index.setter
    def log_index(self, log_index):
        """Sets the log_index of this IERC20Transfer.


        :param log_index: The log_index of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if log_index is None:
            raise ValueError("Invalid value for `log_index`, must not be `None`")  # noqa: E501

        self._log_index = log_index

    @property
    def tag(self):
        """Gets the tag of this IERC20Transfer.  # noqa: E501


        :return: The tag of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this IERC20Transfer.


        :param tag: The tag of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def _from(self):
        """Gets the _from of this IERC20Transfer.  # noqa: E501


        :return: The _from of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this IERC20Transfer.


        :param _from: The _from of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this IERC20Transfer.  # noqa: E501


        :return: The to of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this IERC20Transfer.


        :param to: The to of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def value(self):
        """Gets the value of this IERC20Transfer.  # noqa: E501


        :return: The value of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IERC20Transfer.


        :param value: The value of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def token_decimals(self):
        """Gets the token_decimals of this IERC20Transfer.  # noqa: E501


        :return: The token_decimals of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._token_decimals

    @token_decimals.setter
    def token_decimals(self, token_decimals):
        """Sets the token_decimals of this IERC20Transfer.


        :param token_decimals: The token_decimals of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if token_decimals is None:
            raise ValueError("Invalid value for `token_decimals`, must not be `None`")  # noqa: E501

        self._token_decimals = token_decimals

    @property
    def token_name(self):
        """Gets the token_name of this IERC20Transfer.  # noqa: E501


        :return: The token_name of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this IERC20Transfer.


        :param token_name: The token_name of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if token_name is None:
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def token_symbol(self):
        """Gets the token_symbol of this IERC20Transfer.  # noqa: E501


        :return: The token_symbol of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._token_symbol

    @token_symbol.setter
    def token_symbol(self, token_symbol):
        """Sets the token_symbol of this IERC20Transfer.


        :param token_symbol: The token_symbol of this IERC20Transfer.  # noqa: E501
        :type: str
        """
        if token_symbol is None:
            raise ValueError("Invalid value for `token_symbol`, must not be `None`")  # noqa: E501

        self._token_symbol = token_symbol

    @property
    def value_with_decimals(self):
        """Gets the value_with_decimals of this IERC20Transfer.  # noqa: E501


        :return: The value_with_decimals of this IERC20Transfer.  # noqa: E501
        :rtype: str
        """
        return self._value_with_decimals

    @value_with_decimals.setter
    def value_with_decimals(self, value_with_decimals):
        """Sets the value_with_decimals of this IERC20Transfer.


        :param value_with_decimals: The value_with_decimals of this IERC20Transfer.  # noqa: E501
        :type: str
        """

        self._value_with_decimals = value_with_decimals

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
        if issubclass(IERC20Transfer, dict):
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
        if not isinstance(other, IERC20Transfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
