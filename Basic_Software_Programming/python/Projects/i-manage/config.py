# /config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+pymysql://username:password@localhost/DB' #change this line
    SQLALCHEMY_TRACK_MODIFICATIONS = False


 