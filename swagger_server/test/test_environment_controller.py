# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.image_info import ImageInfo  # noqa: E501
from swagger_server.models.temperature_summary import TemperatureSummary  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEnvironmentController(BaseTestCase):
    """EnvironmentController integration test stubs"""

    def test_set_heater_state(self):
        """Test case for set_heater_state

        
        """
        body = ImageInfo()
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/image/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_temperature_summary(self):
        """Test case for temperature_summary

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/image',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
