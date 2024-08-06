import os

class Config:
    SECRET_KEY = os.urandom(24)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'teste'
    MYSQL_PASSWORD = 'teste'
    MYSQL_DB = 'task_manager'
    MYSQL_CURSORCLASS = 'DictCursor'
    REDIS_URL = "redis://localhost:6379/0"

