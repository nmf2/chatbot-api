# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnswersController(BaseTestCase):
    """AnswersController integration test stubs"""

    def test_answers_get(self):
        """Test case for answers_get

        Get answer from chatbot
        """
        query_string = [('q', 'q_example')]
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/answers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
