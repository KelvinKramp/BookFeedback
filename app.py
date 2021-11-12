import dash
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
import configparser
import os
import json

if "Users" in os.getcwd():
  secrets = 'secrets.json'
  with open(secrets) as f:
      secret = json.load(f)
  # create Google app & get app ID/secret from:
  # https://cloud.google.com/console
  SQL_URI = secret["SQL_URI"]
else:
  SQL_URI = os.environ['SQL_URI']



app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.FLATLY])
server = app.server
config = configparser.ConfigParser()
server.config.update(
    SECRET_KEY=os.urandom(12),
    SQLALCHEMY_DATABASE_URI=SQL_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(server)
db.init_app(server)

class Feedback(db.Model):
    __tablename__ = 'feedback_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False)
    email = db.Column(db.String(200), unique=True)
    Q_C1 = db.Column(db.Integer)
    Q_C2 = db.Column(db.Integer)
    Q_C3 = db.Column(db.Integer)
    Q_C4 = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, name, email, Q_C1, Q_C2, Q_C3, Q_C4, comments):
        self.name = name
        self.email = email
        self.Q_C1 = db.Column(db.Integer)
        self.Q_C2 = db.Column(db.Integer)
        self.Q_C3 = db.Column(db.Integer)
        self.Q_C4 = db.Column(db.Integer)
        self.comments = db.Column(db.Text())
