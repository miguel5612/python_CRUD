import os 
   
   
class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pass@localhost:3306/dbName'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'amqp://localhost//'
    CELERY_RESULT_BACKEND = 'amqp://localhost//'