# import connexion
from swagger_server.models.error import Error  # noqa: E501
# from swagger_server.models.training_questions import TrainingQuestions
from swagger_server import util

from eva.config import BOT_PATH

from pathlib import Path


def training_get():  # noqa: E501
    """Get training questions for each intent

     # noqa: E501


    :rtype: List[TrainingQuestions]
    """
    tqs = util.get_trainning_questions()

    if tqs == []:
        return "No training questions found", 404

    return tqs, 200


def _write_questions(body, mode):
    for tqs in body:
        filename = '/'.join(BOT_PATH, 'data/iob', tqs['intent'], '.iob')
        path = Path(filename)

        if (path.exists()):
            return Error(description="The intent {} already has it's training \
            data. Use PUT to append or update.".format(tqs['intent']),
                         error='data-confict'), 409

        with path.open(mode=mode) as file:
            file.write('\n'.join(tqs['questions']))

    return "Training data was successfully received", 200


def training_post(body):  # noqa: E501
    """Add intents with training questions

     # noqa: E501

    :param body: Array of JSON Objects each with an intent and an array
        of questions
    :type body: list | bytes

    :rtype: None
    """

    return _write_questions(body, 'w+')


def training_put(body, append):  # noqa: E501
    """Append or update training questions for each intent

     # noqa: E501

    :param body: Array of JSON Objects each with an intent and an array
        of questions to substitute the present training data
    :type body: list | bytes
    :param append: Defines if the incoming training data should replace
        or append the  original data
    :type append: bool

    :rtype: None
    """

    return _write_questions(body, 'a+')
