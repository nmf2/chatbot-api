from swagger_server.models.answer import Answer  # noqa: E501
from eva.responses import Respondent
from eva.utils.parser import parse


def answers_get(q):  # noqa: E501
    """Get answer from chatbot

     # noqa: E501

    :param q: question to be answered
    :type q: str

    :rtype: Answer
    """
    question = parse(q)
    res = Respondent()
    ans = res.answer(question)
    return Answer(ans), 200
