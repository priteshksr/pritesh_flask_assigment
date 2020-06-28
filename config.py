import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ksfdbcuweducdudncdc'
    #SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:5432/{}".format(environ.get('DB_USER'), environ.get('DB_PASSWORD'), environ.get('DB_HOST'), environ.get('DB_NAME'))
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql:///flask_new_2'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'ksfdbcuweducdudncdc'
    #SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:5432/{}".format(environ.get('DB_USER'), environ.get('DB_PASSWORD'), environ.get('DB_HOST'), environ.get('DB_NAME'))
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/postgres_test"