# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.train_info import TrainInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainController(BaseTestCase):
    """TrainController integration test stubs"""

    def test_train_get(self):
        """Test case for train_get

        
        """
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/train',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_train_post(self):
        """Test case for train_post

        
        """
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/train',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
