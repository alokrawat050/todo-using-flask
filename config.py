import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'Xdwewqesd123131!CFVFr453453g11'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
