import connexion
import six

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.training_questions import TrainingQuestions  # noqa: E501
from swagger_server import util


def training_get():  # noqa: E501
    """Get training questions for each intent

     # noqa: E501


    :rtype: List[TrainingQuestions]
    """
    return 'do some magic!'


def training_post(body):  # noqa: E501
    """Add intents with training questions

     # noqa: E501

    :param body: Array of JSON Objects each with an intent and an array of questions
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [TrainingQuestions.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def training_put(body, append):  # noqa: E501
    """Append or update training questions for each intent

     # noqa: E501

    :param body: Array of JSON Objects each with an intent and an array of questions to substitute the present training data 
    :type body: list | bytes
    :param append: Defines if the incoming training data should replace or append the  original data 
    :type append: bool

    :rtype: None
    """
    if connexion.request.is_json:
        body = [TrainingQuestions.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
