from os import environ

MONGO_URL = environ.get('MONGO_URL', '')
