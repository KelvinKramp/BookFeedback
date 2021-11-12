from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()

SQL_URI = "postgres://ltrredytatniha:3a13463b7d0e4a6623e98617fad31de2ea8ad72051496180daa3b6340d06ccd3@ec2-52-209-246-87.eu-west-1.compute.amazonaws.com:5432/dbfi85qqp960ge"

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
