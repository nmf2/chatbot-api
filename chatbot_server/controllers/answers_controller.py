from chatbot_server.models.answer import Answer  # noqa: E501
from eva.responses import Respondent
from eva.utils.parser import parse


def answers_get(q):  # noqa: E501
    """Get answer from chatbot

     # noqa: E501

    :param q: question to be answered
    :type q: str

    :rtype: Answer
    """
    
    code = 404
    response = None
    try:
        question = parse(q)
        respondent = Respondent()
        ans = respondent.answer(question)
        response = Answer(ans)
        code = 200
    except(Exception):
        pass

    return response, code
