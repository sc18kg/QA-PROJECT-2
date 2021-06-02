  from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(50), nullable=False)