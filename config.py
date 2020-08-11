import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    secretKey = os.environ.get('SECRET_KEY') or 'yo54u-wi5ll-neve52r-gu#$ess'
    sqlAlchemyDatabaseUri = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'budgetapp.db')
    mailServer = os.environ.get('MAIL_SERVER')
    mailPort = int(os.environ.get('MAIL_PORT') or 25)
    mailUseTls = os.environ.get('MAIL_USE_TLS') is not None
    mailUsername = os.environ.get('MAIL_USERNAME')
    mailPassword = os.environ.get('MAIL_PASSWORD')
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    admins = ['antoineg.simard@gmail.com']
    testing = False
