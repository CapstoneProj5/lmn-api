
import os


class Config(object):

    SECRET_KEY = os.urandom(27)
    DEBUG = False
    TESTING = False
    DATABASE_URI = None


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    

class TestingConfig(Config):
    TESTING = True


del os
