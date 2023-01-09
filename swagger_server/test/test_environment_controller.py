# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.forecast_response import ForecastResponse  # noqa: E501
from swagger_server.models.heater_state import HeaterState  # noqa: E501
from swagger_server.models.temperatue_zone_status import TemperatueZoneStatus  # noqa: E501
from swagger_server.models.temperature_summary import TemperatureSummary  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEnvironmentController(BaseTestCase):
    """EnvironmentController integration test stubs"""

    def test_get_forecast(self):
        """Test case for get_forecast

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/temperature/forecast/{days}'.format(days=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_heater_state(self):
        """Test case for get_heater_state

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/temperature/{zoneId}/heater'.format(zone_id='zone_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_zone_temperature(self):
        """Test case for get_zone_temperature

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/temperature/{zoneId}'.format(zone_id='zone_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_heater_state(self):
        """Test case for set_heater_state

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/temperature/{zoneId}/heater/{state}'.format(zone_id='zone_id_example', state='state_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_temperature_summary(self):
        """Test case for temperature_summary

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/temperature',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
