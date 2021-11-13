import dash
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
import configparser
import os
import json

# MAKE DIFFERENCE BETWEEN PRODUCTION AND DEVELOPMENT ENVIRONMENT
if "Users" in os.getcwd():
  secrets = 'secrets.json'
  with open(secrets) as f:
      secret = json.load(f)
  SQL_URI = secret["SQL_URI"]
else:
  SQL_URI = os.environ['SQL_URI']

# START APP
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# CONFIGURE DATABASE
config = configparser.ConfigParser()
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=SQL_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(server)
db.init_app(server)

# CREATE DATABASE TABLE
class Feedback(db.Model):
    __tablename__ = 'feedback_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=True)
    Q_C1 = db.Column(db.Integer)
    # Q_C2 = db.Column(db.Integer)
    # Q_C3 = db.Column(db.Integer)
    # Q_C4 = db.Column(db.Integer)
    # Q_C5 = db.Column(db.Integer)
    # Q_C6 = db.Column(db.Integer)
    # Q_C7 = db.Column(db.Integer)
    # Q_open1 = db.Column(db.String(1000), unique=False)
    # Q_open2 = db.Column(db.String(1000), unique=False)
    # Q_open3 = db.Column(db.String(1000), unique=False)
    # Q_open4 = db.Column(db.String(1000), unique=False)
    # Q_open5 = db.Column(db.String(1000), unique=False)
    # Q_open6 = db.Column(db.String(1000), unique=False)
    # Q_open7 = db.Column(db.String(1000), unique=False)
