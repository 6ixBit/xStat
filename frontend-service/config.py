import os

class Config(object):
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'