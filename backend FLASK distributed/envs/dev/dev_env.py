import os
from dotenv import load_dotenv

load_dotenv()


class DevConfig:
    DEBUG = os.getenv('DEBUG_MODE')


config = {
    'dev': DevConfig
}


def get_database_config():
    database_config = {
        'MYSQL_HOST': os.getenv('MYSQL_HOST'),
        'MYSQL_USER': os.getenv('MYSQL_USER'),
        'MYSQL_PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'DATABASE_NAME': os.getenv('DATABASE_NAME'),
        'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    }
    return database_config
