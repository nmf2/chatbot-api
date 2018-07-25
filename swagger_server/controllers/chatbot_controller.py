import connexion
import six

from swagger_server.models.chatbot import Chatbot  # noqa: E501
from swagger_server import util


def root_get():  # noqa: E501
    """chatbot information

     # noqa: E501


    :rtype: Chatbot
    """
    return 'do some magic!'
