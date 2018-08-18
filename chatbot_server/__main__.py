#!/usr/bin/env python3

import connexion

from chatbot_server import encoder
from waitress import serve

import logging


def main():
    logging.basicConfig(level=logging.INFO)
    # To run locally:
    # app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    # To run on docker:
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Chatbot API'})
    app.run(port=8080, debug=True)
    # serve(app)


if __name__ == '__main__':
    main()
