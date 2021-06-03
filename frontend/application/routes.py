from flask import Flask, render_template, redirect, url_for, request
import requests
from flask_sqlalchemy import SQLAlchemy
from application.models import Character, UsersForm
from application import app, db
import os, random, requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SHH')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UsersForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data

    race = requests.get("http://app-2:5001/race")
    gender = requests.get("http://app-3:5002/gender")
    dictionary = {'race': race.text, 'gender': gender.text}
    skills = requests.post("http://app-4:5003/skills", json=dictionary)

    db_info = Character(race=race.text, gender=gender.text, skills=skills.text)
    db.session.add(db_info)
    db.session.commit()

    return render_template('index.html', race=race, gender=gender, skills=skills, form=form)
