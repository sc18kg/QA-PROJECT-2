from flask import Flask, render_template, redirect, url_for, request
import requests
from application.models import Character
from application import app, db

@app.route('/', methods=['GET', 'POST'])
def index():
    race = requests.get("http://app-2:5001/race")
    gender = requests.get("http://app-3:5002/gender")
    dictionary = {'race': race.text, 'gender': gender.text}
    skills = requests.post("http://app-4:5003/skills", json=dictionary)

    db_info = Character(race=race.text, gender=gender.text, skills=skills.text)
    db.session.add(db_info)
    db.session.commit()

    return render_template('index.html', race=race.text, gender=gender.text, skills=skills.text)
