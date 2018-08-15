# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from chatbot_server.models.chatbot import Chatbot  # noqa: E501
from chatbot_server.test import BaseTestCase


class TestChatbotController(BaseTestCase):
    """ChatbotController integration test stubs"""

    def test_root_get(self):
        """Test case for root_get

        chatbot information
        """
        response = self.client.open(
            '/nmf21/chatbotModel/1.0.0/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
