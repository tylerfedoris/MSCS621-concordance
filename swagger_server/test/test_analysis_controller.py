# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.location_result import LocationResult  # noqa: E501
from swagger_server.models.result import Result  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnalysisController(BaseTestCase):
    """AnalysisController integration test stubs"""

    def test_get_concordance(self):
        """Test case for get_concordance

        Calculate
        """
        body = '\"The brown fox jumped over the brown log.\"'
        response = self.client.open(
            '/mscs621/tfedoris/concordance/2.0.0/analyze',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_concordance_with_location(self):
        """Test case for get_concordance_with_location

        Calculate Location
        """
        body = '\"The brown fox jumped over the brown log.\"'
        response = self.client.open(
            '/mscs621/tfedoris/concordance/2.0.0/analyze_location',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
