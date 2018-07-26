from connexion import NoContent
from swagger_server.models.train_info import TrainInfo

from eva.config import BOT_PATH
from eva.entities.train import IOBTagger
from eva.intents.train import IntentClassifier
from datetime import datetime

from pathlib import Path
from os import path
from glob import glob

from collections import defaultdict

import json


def train_get():
    """train_get

    Get information about the training # noqa: E501


    :rtype: TrainInfo
    """
    return 'do some magic!'


def train_post():  # noqa: E501
    """train_post

    Actually train the chatbot model on the server # noqa: E501


    :rtype: None
    """
    if glob('/'.join(BOT_PATH, 'data/iob', '*.iob')) == []:
        return "No training data found", 404

    try:
        info_file = open('info.json', 'a+')
        info_file.seek(0)
        info = defaultdict(str, json.load(info_file))
        info_file.seek(0)
        info['finished'] = False

        tagger = IOBTagger()
        tagger.train()
        info['finished'] = True
        info['created'] = datetime.now()
        json.dump(info, info_file)
        info_file.close()
    except(Exception):
        return "Training failed in the server", 500
    
    return "Training finished sucessfully", 200
