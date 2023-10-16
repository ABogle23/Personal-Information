from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_height = request.form.get("height")
    yearOB = (2023 - int(input_age))
    return render_template("hello.html", name=input_name, height=input_height, age=input_age, year_of_birth=yearOB)