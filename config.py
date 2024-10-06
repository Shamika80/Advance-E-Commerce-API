import os
from datetime import timedelta
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://your_username:your_password@your_host/your_database' 
SQLALCHEMY_TRACK_MODIFICATIONS = False
CACHE_TYPE = 'simple'
JWT_SECRET_KEY = 'your-jwt-secret-key'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) 