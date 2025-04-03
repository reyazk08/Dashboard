import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///trading_bot.db'
    API_KEY = os.environ.get('API_KEY') or 'your_api_key'
    TIMEZONE = os.environ.get('TIMEZONE') or 'UTC'
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'INFO'