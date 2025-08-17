from os import environ, path
from dotenv import load_dotenv
import yaml
import logging

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Load DB config: prefer db.yaml, fall back to db.yaml.example.
# Use safe_load and full paths to avoid FileNotFoundError and yaml warnings.
db = {}
db_path = path.join(basedir, 'db.yaml')
db_example_path = path.join(basedir, 'db.yaml.example')
for p in (db_path, db_example_path):
    if path.exists(p):
        try:
            with open(p, 'r') as fh:
                db = yaml.safe_load(fh) or {}
        except Exception as e:
            logging.warning("Failed to load DB config from %s: %s", p, e)
        break
else:
    logging.warning("No db.yaml or db.yaml.example found; proceeding with empty DB config.")


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    # Ensure SESSION_COOKIE_NAME has a default; if env not provided, use Flask's default 'session'.
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME', 'session')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # add database for production here


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    MYSQL_HOST = db.get('mysql_host')
    MYSQL_USER = db.get('mysql_user')
    MYSQL_PASSWORD = db.get('mysql_password')
    MYSQL_DB = db.get('mysql_db')
    
