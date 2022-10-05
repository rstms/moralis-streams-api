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

class INFTTransfer(object):
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
        'token_contract_type': 'str',
        'token_name': 'str',
        'token_symbol': 'str',
        'operator': 'str',
        '_from': 'str',
        'to': 'str',
        'token_id': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'transaction_hash': 'transactionHash',
        'contract': 'contract',
        'log_index': 'logIndex',
        'tag': 'tag',
        'token_contract_type': 'tokenContractType',
        'token_name': 'tokenName',
        'token_symbol': 'tokenSymbol',
        'operator': 'operator',
        '_from': 'from',
        'to': 'to',
        'token_id': 'tokenId',
        'amount': 'amount'
    }

    def __init__(self, transaction_hash=None, contract=None, log_index=None, tag=None, token_contract_type=None, token_name=None, token_symbol=None, operator=None, _from=None, to=None, token_id=None, amount=None):  # noqa: E501
        """INFTTransfer - a model defined in Swagger"""  # noqa: E501
        self._transaction_hash = None
        self._contract = None
        self._log_index = None
        self._tag = None
        self._token_contract_type = None
        self._token_name = None
        self._token_symbol = None
        self._operator = None
        self.__from = None
        self._to = None
        self._token_id = None
        self._amount = None
        self.discriminator = None
        self.transaction_hash = transaction_hash
        self.contract = contract
        self.log_index = log_index
        self.tag = tag
        self.token_contract_type = token_contract_type
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.operator = operator
        self._from = _from
        self.to = to
        self.token_id = token_id
        self.amount = amount

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this INFTTransfer.  # noqa: E501


        :return: The transaction_hash of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this INFTTransfer.


        :param transaction_hash: The transaction_hash of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def contract(self):
        """Gets the contract of this INFTTransfer.  # noqa: E501


        :return: The contract of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this INFTTransfer.


        :param contract: The contract of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if contract is None:
            raise ValueError("Invalid value for `contract`, must not be `None`")  # noqa: E501

        self._contract = contract

    @property
    def log_index(self):
        """Gets the log_index of this INFTTransfer.  # noqa: E501


        :return: The log_index of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._log_index

    @log_index.setter
    def log_index(self, log_index):
        """Sets the log_index of this INFTTransfer.


        :param log_index: The log_index of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if log_index is None:
            raise ValueError("Invalid value for `log_index`, must not be `None`")  # noqa: E501

        self._log_index = log_index

    @property
    def tag(self):
        """Gets the tag of this INFTTransfer.  # noqa: E501


        :return: The tag of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this INFTTransfer.


        :param tag: The tag of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def token_contract_type(self):
        """Gets the token_contract_type of this INFTTransfer.  # noqa: E501


        :return: The token_contract_type of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._token_contract_type

    @token_contract_type.setter
    def token_contract_type(self, token_contract_type):
        """Sets the token_contract_type of this INFTTransfer.


        :param token_contract_type: The token_contract_type of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if token_contract_type is None:
            raise ValueError("Invalid value for `token_contract_type`, must not be `None`")  # noqa: E501

        self._token_contract_type = token_contract_type

    @property
    def token_name(self):
        """Gets the token_name of this INFTTransfer.  # noqa: E501


        :return: The token_name of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this INFTTransfer.


        :param token_name: The token_name of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if token_name is None:
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def token_symbol(self):
        """Gets the token_symbol of this INFTTransfer.  # noqa: E501


        :return: The token_symbol of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._token_symbol

    @token_symbol.setter
    def token_symbol(self, token_symbol):
        """Sets the token_symbol of this INFTTransfer.


        :param token_symbol: The token_symbol of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if token_symbol is None:
            raise ValueError("Invalid value for `token_symbol`, must not be `None`")  # noqa: E501

        self._token_symbol = token_symbol

    @property
    def operator(self):
        """Gets the operator of this INFTTransfer.  # noqa: E501


        :return: The operator of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this INFTTransfer.


        :param operator: The operator of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def _from(self):
        """Gets the _from of this INFTTransfer.  # noqa: E501


        :return: The _from of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this INFTTransfer.


        :param _from: The _from of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this INFTTransfer.  # noqa: E501


        :return: The to of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this INFTTransfer.


        :param to: The to of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def token_id(self):
        """Gets the token_id of this INFTTransfer.  # noqa: E501


        :return: The token_id of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this INFTTransfer.


        :param token_id: The token_id of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def amount(self):
        """Gets the amount of this INFTTransfer.  # noqa: E501


        :return: The amount of this INFTTransfer.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this INFTTransfer.


        :param amount: The amount of this INFTTransfer.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

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
        if issubclass(INFTTransfer, dict):
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
        if not isinstance(other, INFTTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
