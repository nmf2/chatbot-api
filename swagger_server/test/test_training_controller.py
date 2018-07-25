# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.training_questions import TrainingQuestions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainingController(BaseTestCase):
    """TrainingController integration test stubs"""

    def test_training_get(self):
        """Test case for training_get

        Get training questions for each intent
        """
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/training',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_training_post(self):
        """Test case for training_post

        Add intents with training questions
        """
        body = [TrainingQuestions()]
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/training',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_training_put(self):
        """Test case for training_put

        Append or update training questions for each intent
        """
        body = [TrainingQuestions()]
        query_string = [('append', true)]
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/training',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
