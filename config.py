import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
NAME = os.environ.get('NAME')
PASSWORD = os.environ.get('PASSWORD')
USER = os.environ.get('USER')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')


