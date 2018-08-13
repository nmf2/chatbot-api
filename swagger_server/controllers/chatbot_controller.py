from swagger_server.models.chatbot import Chatbot  # noqa: E501
from eva.config import BOT_PATH
import json


def root_get():  # noqa: E501
    """chatbot information

     # noqa: E501


    :rtype: Chatbot
    """
    try:
        info = json.load(open(BOT_PATH+'/info.json'))
        res = Chatbot(**info)
        code = 200
    except(Exception):
        res = "No information file"
        code = 500
    
    return res, code
