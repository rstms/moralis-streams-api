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

class INFTApprovalERC721(object):
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
        'token_address': 'str',
        'log_index': 'str',
        'tag': 'str',
        'owner': 'str',
        'approved': 'str',
        'token_id': 'str',
        'token_contract_type': 'str',
        'token_name': 'str',
        'token_symbol': 'str'
    }

    attribute_map = {
        'transaction_hash': 'transactionHash',
        'token_address': 'tokenAddress',
        'log_index': 'logIndex',
        'tag': 'tag',
        'owner': 'owner',
        'approved': 'approved',
        'token_id': 'tokenId',
        'token_contract_type': 'tokenContractType',
        'token_name': 'tokenName',
        'token_symbol': 'tokenSymbol'
    }

    def __init__(self, transaction_hash=None, token_address=None, log_index=None, tag=None, owner=None, approved=None, token_id=None, token_contract_type=None, token_name=None, token_symbol=None):  # noqa: E501
        """INFTApprovalERC721 - a model defined in Swagger"""  # noqa: E501
        self._transaction_hash = None
        self._token_address = None
        self._log_index = None
        self._tag = None
        self._owner = None
        self._approved = None
        self._token_id = None
        self._token_contract_type = None
        self._token_name = None
        self._token_symbol = None
        self.discriminator = None
        self.transaction_hash = transaction_hash
        self.token_address = token_address
        self.log_index = log_index
        self.tag = tag
        self.owner = owner
        self.approved = approved
        self.token_id = token_id
        self.token_contract_type = token_contract_type
        self.token_name = token_name
        self.token_symbol = token_symbol

    @property
    def transaction_hash(self):
        """Gets the transaction_hash of this INFTApprovalERC721.  # noqa: E501


        :return: The transaction_hash of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash):
        """Sets the transaction_hash of this INFTApprovalERC721.


        :param transaction_hash: The transaction_hash of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def token_address(self):
        """Gets the token_address of this INFTApprovalERC721.  # noqa: E501


        :return: The token_address of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._token_address

    @token_address.setter
    def token_address(self, token_address):
        """Sets the token_address of this INFTApprovalERC721.


        :param token_address: The token_address of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if token_address is None:
            raise ValueError("Invalid value for `token_address`, must not be `None`")  # noqa: E501

        self._token_address = token_address

    @property
    def log_index(self):
        """Gets the log_index of this INFTApprovalERC721.  # noqa: E501


        :return: The log_index of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._log_index

    @log_index.setter
    def log_index(self, log_index):
        """Sets the log_index of this INFTApprovalERC721.


        :param log_index: The log_index of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if log_index is None:
            raise ValueError("Invalid value for `log_index`, must not be `None`")  # noqa: E501

        self._log_index = log_index

    @property
    def tag(self):
        """Gets the tag of this INFTApprovalERC721.  # noqa: E501


        :return: The tag of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this INFTApprovalERC721.


        :param tag: The tag of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def owner(self):
        """Gets the owner of this INFTApprovalERC721.  # noqa: E501


        :return: The owner of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this INFTApprovalERC721.


        :param owner: The owner of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def approved(self):
        """Gets the approved of this INFTApprovalERC721.  # noqa: E501


        :return: The approved of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this INFTApprovalERC721.


        :param approved: The approved of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if approved is None:
            raise ValueError("Invalid value for `approved`, must not be `None`")  # noqa: E501

        self._approved = approved

    @property
    def token_id(self):
        """Gets the token_id of this INFTApprovalERC721.  # noqa: E501


        :return: The token_id of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id):
        """Sets the token_id of this INFTApprovalERC721.


        :param token_id: The token_id of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501

        self._token_id = token_id

    @property
    def token_contract_type(self):
        """Gets the token_contract_type of this INFTApprovalERC721.  # noqa: E501


        :return: The token_contract_type of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._token_contract_type

    @token_contract_type.setter
    def token_contract_type(self, token_contract_type):
        """Sets the token_contract_type of this INFTApprovalERC721.


        :param token_contract_type: The token_contract_type of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if token_contract_type is None:
            raise ValueError("Invalid value for `token_contract_type`, must not be `None`")  # noqa: E501

        self._token_contract_type = token_contract_type

    @property
    def token_name(self):
        """Gets the token_name of this INFTApprovalERC721.  # noqa: E501


        :return: The token_name of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._token_name

    @token_name.setter
    def token_name(self, token_name):
        """Sets the token_name of this INFTApprovalERC721.


        :param token_name: The token_name of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if token_name is None:
            raise ValueError("Invalid value for `token_name`, must not be `None`")  # noqa: E501

        self._token_name = token_name

    @property
    def token_symbol(self):
        """Gets the token_symbol of this INFTApprovalERC721.  # noqa: E501


        :return: The token_symbol of this INFTApprovalERC721.  # noqa: E501
        :rtype: str
        """
        return self._token_symbol

    @token_symbol.setter
    def token_symbol(self, token_symbol):
        """Sets the token_symbol of this INFTApprovalERC721.


        :param token_symbol: The token_symbol of this INFTApprovalERC721.  # noqa: E501
        :type: str
        """
        if token_symbol is None:
            raise ValueError("Invalid value for `token_symbol`, must not be `None`")  # noqa: E501

        self._token_symbol = token_symbol

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
        if issubclass(INFTApprovalERC721, dict):
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
        if not isinstance(other, INFTApprovalERC721):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
