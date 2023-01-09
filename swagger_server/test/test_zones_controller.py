# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestZonesController(BaseTestCase):
    """ZonesController integration test stubs"""

    def test_get_zones(self):
        """Test case for get_zones

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/zones',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_quiet_zone(self):
        """Test case for quiet_zone

        
        """
        response = self.client.open(
            '/HANNESSOFTWARE/imaginAIry/1.0.0/zones/{zoneId}/quiet'.format(zone_id='zone_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
