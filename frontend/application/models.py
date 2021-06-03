from application import db
from flask import render_template, request, redirect, url_for, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(1000), nullable=False)

class UsersForm(FlaskForm):
    name = StringField("Enter your name:",
        validators = [DataRequired(message='Field Required'),
        Length(max=20,min=1)])
    sbmit = SubmitField("Submit")