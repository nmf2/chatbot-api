from chatbot_server.models.chatbot import Chatbot  # noqa: E501
from eva.config import BOT_PATH
import json


def root_get():  # noqa: E501
    """chatbot information

     # noqa: E501


    :rtype: Chatbot
    """
    info = json.load(open(BOT_PATH+'/info.json'))
    
    # return Chatbot(**info), 200
    return info, 200
