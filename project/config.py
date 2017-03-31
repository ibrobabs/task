import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'taskr.db'
CSRF_ENABLED = True
SECRET_KEY = "SECRET"

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = False