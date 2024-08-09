# /config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+pymysql://teste:teste@localhost/life_management_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


 