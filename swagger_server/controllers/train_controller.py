from swagger_server import util
from swagger_server.models.train_info import TrainInfo

from eva.config import BOT_PATH
from eva.entities.train import IOBTagger
from eva.intents.train import IntentClassifier
from datetime import datetime

from glob import glob

from collections import defaultdict
from pathlib import Path

import json


def train_get():
    """train_get

    Get information about the training # noqa: E501


    :rtype: TrainInfo
    """
    try:
        build_file = _get_build_file()
        info = defaultdict(str, json.load(build_file))
        info['training_data'] = util.get_training_questions()
        build_file.close()
    except(Exception):
        raise
        return "Server error", 500

    return TrainInfo(**info), 200


def train_post():  # noqa: E501
    """train_post

    Actually train the chatbot model on the server # noqa: E501


    :rtype: None
    """
    if glob('/'.join([BOT_PATH, 'data/iob', '*.iob'])) == []:
        return "No training data found", 404

    try:
        info = defaultdict(str)
        info['finished'] = False

        entity_trainer = IOBTagger()
        entity_trainer.train()

        intent_trainer = IntentClassifier()
        intent_trainer.fit()  # train
        intent_trainer.save('intent.model')

        info['finished'] = True
        info['created'] = str(datetime.now())

        build_file = _get_build_file(mode='w+')
        json.dump(info, build_file)
        build_file.close()
    except(Exception):
        raise
        return "Training failed in the server", 500

    return "Training finished sucessfully", 200


def _get_build_file(path=BOT_PATH+'/models/build.json', mode='a+'):
    build_file = Path(path)
    if not build_file.exists():
        build_file.touch()
        build_file.write_text("{}")
    build_file = build_file.open(mode=mode)
    build_file.seek(0)
    return build_file
