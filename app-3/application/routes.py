from flask import Flask, Response, request
import random

from application import app

@app.route('/gender', methods=['GET'])
def gender():
    gender = ['Male', 'Female']
    gender = random.choice(gender)
    return Response(gender, mimetype='text/plain')