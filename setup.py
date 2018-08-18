# coding: utf-8

# import sys
from setuptools import setup, find_packages

NAME = "chatbot_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    zip_safe=False,
    description="Chatbot API",
    author_email="developer@example.com",
    url="",
    keywords=["Swagger", "Chatbot API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    entry_points={
        'console_scripts': ['chatbot_server=chatbot_server.__main__:main']},
    long_description="""\
    This is the API for the Chatbot
    """
)

