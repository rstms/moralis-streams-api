# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import moralis_streams_api
from moralis_streams_api.api.project_api import ProjectApi  # noqa: E501
from moralis_streams_api.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_settings(self):
        """Test case for get_settings

        """
        pass

    def test_set_settings(self):
        """Test case for set_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()