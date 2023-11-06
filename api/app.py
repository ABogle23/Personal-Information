import requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_height = request.form.get("height")
    surface = request.form.get("surface")
    activity = request.form.get("activity")
    storage = request.form.get("storage")
    bicycle_recommendation = ""
    if surface == "Road":
        if storage == "Limited":
            bicycle_recommendation = "Folding Bike"
        elif activity == "Commuting":
            bicycle_recommendation = "Hybrid Bike"
        else:
            bicycle_recommendation = "Road Bike"
    else:
        bicycle_recommendation = "Mountain Bike"
    return render_template(
        "hello.html",
        name=input_name,
        height=input_height,
        surface=surface,
        activity=activity,
        storage=storage,
        bicycle_recommendation=bicycle_recommendation
        )


#github
@app.route("/github")
def github():
    return render_template("github.html")


#github
@app.route("/submit_github", methods=["POST"])
def submit_github():
    github_username = request.form.get("github_username")

    response = requests.get(f"https://api.github.com/users/{github_username}/repos")

    if response.status_code == 200:
        repos = response.json() # data returned is a list of ‘repository’ entities
        for repo in repos:
            print(repo["full_name"])
    else:
        return "Error fetching repos"


    return render_template(
        "github_response.html",
        name=github_username
        )


@app.route("/query", methods=["GET"])
def test_query_return():
    q = request.args.get('q')
    return process_query(q)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
