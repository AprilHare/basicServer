# server configurations

import os

class config(object):
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/basicServer"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'THIS.is;TEMP,whats/aGoodWAy-to.do!it?'


