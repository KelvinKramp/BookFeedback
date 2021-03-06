import dash
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
import configparser
import os
import json
from dotenv import load_dotenv
load_dotenv()

#
# If you dont want people to send their feedback multiple times with the same email address change the  value of unique to True in the classess beneath
#

# LOAD DB URI
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
class Feedback_Book(db.Model):
    __tablename__ = 'feedback_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=False)
    Q_C1 = db.Column(db.Integer, nullable=True)
    Q_C2 = db.Column(db.Integer, nullable=True)
    Q_C3 = db.Column(db.Integer, nullable=True)
    Q_C4 = db.Column(db.Integer, nullable=True)
    Q_C5 = db.Column(db.Integer, nullable=True)
    Q_C6 = db.Column(db.Integer, nullable=True)
    Q_C7 = db.Column(db.Integer, nullable=True)
    Q_C8 = db.Column(db.Integer, nullable=True)
    Q_open1 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open2 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open3 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open4 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open5 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open6 = db.Column(db.String(2000), nullable=True, unique=False)
    Q_open7 = db.Column(db.String(2000), nullable=True, unique=False)
    time = db.Column(db.String(100), unique=False)

class Report_Bug(db.Model):
    __tablename__ = 'report_bug'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=False)
    bug = db.Column(db.String(2000), nullable=True, unique=False)
    time = db.Column(db.String(100), unique=False)

class Buy_Hardcover(db.Model):
    __tablename__ = 'buy_hardcover'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    email = db.Column(db.String(50), unique=False)
    buy = db.Column(db.Boolean, default=False)
    time = db.Column(db.String(100), unique=False)