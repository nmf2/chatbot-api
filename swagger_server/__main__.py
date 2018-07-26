#!/usr/bin/env python3

import connexion

from swagger_server import encoder

import logging


def main():
    logging.basicConfig(level=logging.INFO)
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    # app.add_api('swagger.yaml', arguments={'title': 'Chatbot API'})
    app.add_api('swagger.yaml')
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
