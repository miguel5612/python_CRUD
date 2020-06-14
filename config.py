import os 
   
   
class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://liker:6574*Liker@localhost:3306/aiscrap'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'amqp://localhost//'
    CELERY_RESULT_BACKEND = 'amqp://localhost//'