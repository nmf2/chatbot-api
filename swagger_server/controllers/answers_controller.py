import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server import util


def answers_get(q):  # noqa: E501
    """Get answer from chatbot

     # noqa: E501

    :param q: question to be answered
    :type q: str

    :rtype: Answer
    """
    return 'do some magic!'
