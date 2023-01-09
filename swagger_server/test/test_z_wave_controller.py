# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.device_state import DeviceState  # noqa: E501
from swagger_server.test import BaseTestCase


class TestZWaveController(BaseTestCase):
    """ZWaveController integration test stubs"""

    def test_get_switch_state(self):
        """Test case for get_switch_state

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/lighting/switches/{deviceId}'.format(device_id='device_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_dimmer(self):
        """Test case for set_dimmer

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/lighting/dimmers/{deviceId}/{value}'.format(device_id='device_id_example', value=100),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_dimmer_timer(self):
        """Test case for set_dimmer_timer

        
        """
        query_string = [('units', 'milliseconds')]
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/lighting/dimmers/{deviceId}/{value}/timer/{timeunit}'.format(device_id='device_id_example', value=56, timeunit=56),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_switch(self):
        """Test case for set_switch

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/lighting/switches/{deviceId}/{value}'.format(device_id='device_id_example', value='value_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_switch_timer(self):
        """Test case for set_switch_timer

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/lighting/switches/{deviceId}/{value}/timer/{minutes}'.format(device_id='device_id_example', value='value_example', minutes=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
