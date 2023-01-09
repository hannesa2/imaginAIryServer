# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device_registration_info import DeviceRegistrationInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDeviceController(BaseTestCase):
    """DeviceController integration test stubs"""

    def test_get_devices(self):
        """Test case for get_devices

        
        """
        query_string = [('skip', 56),
                        ('limit', 56)]
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/devices',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register(self):
        """Test case for register

        
        """
        body = DeviceRegistrationInfo()
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/devices',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
