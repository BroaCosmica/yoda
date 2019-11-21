import os

SECRET_KEY = 'you_will_never_guess' 
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'fox123'
DATABASE_NAME = 'yoda'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI = 'mysql+pymysql://%s:%s@%s/%s' %(DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True