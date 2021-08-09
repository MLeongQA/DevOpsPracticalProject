from . import db

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    pass_score = db.Column(db.Integer)
    usage = db.Column(db.String(12), default="Not in Use")

