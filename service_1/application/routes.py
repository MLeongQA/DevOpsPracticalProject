from flask import render_template, redirect, request, url_for
import requests

from . import app, db
from .models import Password
from .forms import PassLengthForm

@app.route("/")
@app.route("/index")
def index():
    pass_record = Password.query.all()
    return render_template("index.html", pass_record=pass_record)

@app.route("/create", methods=["GET", "POST"])
def create():
    pass_form = PassLengthForm()

    if request.method == "POST":
        pass_length = pass_form.pass_length.data
        rand_string = requests.post("http://service-2:5000/post/string", json=pass_length).text
        rand_int = requests.get("http://service-3:5000/get/num").text

        gen_pass = rand_string + rand_int

        score = requests.post("http://service-4:5000/post/password", data=gen_pass).json()

        new_pass = Password(password=gen_pass, pass_score=score)
        db.session.add(new_pass)
        db.session.commit()

        return redirect(url_for("index"))

    else:
        return render_template("create.html", form=pass_form)

@app.route("/update/<int:id>")
def update(id):
    password = Password.query.get(id)

    if password.usage == "Not in Use":
        password.usage = "In Use"
    else:
        password.usage = "Not in Use"

    db.session.add(password)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    password = Password.query.get(id)
    #password_list = Password.query.filter(id==id).delete()
    
    db.session.delete(password) 
    db.session.commit()

    return redirect(url_for("index"))

    