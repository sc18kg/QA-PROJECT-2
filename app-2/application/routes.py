from flask import Flask, Response, request
import random

from application import app

@app.route('/race', methods=['GET'])
def race():
    race = ['Altmer', 'Argonian', 'Bosmer', 'Breton', 'Dunmer', 'Imperial', 'Khajiit', 'Nord', 'Orc', 'Redguard']
    race = random.choice(race)
    return Response(race, mimetype='text/plain')