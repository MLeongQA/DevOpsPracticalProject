from flask import render_template
import requests

from . import app, db
from .models import Password

@app.route("/")
def index():
    rand_string = requests.get("http://service-2:5000/get/string").text
    rand_int = requests.get("http://service-3:5000/get/num").text

    gen_pass = rand_string + rand_int
    score = requests.post("http://service-4:5000/post/password", data=gen_pass).json()

    pass_record = Password.query.all()

    new_pass = Password(password=gen_pass, pass_score=score)
    db.session.add(new_pass)
    db.session.commit()

    return render_template("index.html", pass_record=pass_record)

