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


@app.route("/github")
def github():
    return render_template("github.html")


@app.route("/submit_github", methods=["POST"])
def submit_github():
    github_username = request.form.get("github_username")

    response = requests.get(
        f"https://api.github.com/users/{github_username}/repos", timeout=10)

    if response.status_code == 200:
        repos = response.json()
        repo_details = []

        for repo in repos:
            repo_name = repo["full_name"]
            last_updated = repo["updated_at"]
            commits_url = f"https://api.github.com/repos/{repo_name}/commits"
            commits_response = requests.get(commits_url, timeout=10)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                if commits:
                    latest_commit = commits[0]
                    commit_hash = latest_commit["sha"]
                    author = latest_commit["commit"]["author"]["name"]
                    commit_date = latest_commit["commit"]["author"]["date"]
                    commit_message = latest_commit["commit"]["message"]

                    repo_details.append({
                        "name": repo_name,
                        "last_updated": last_updated,
                        "commit_hash": commit_hash,
                        "author": author,
                        "commit_date": commit_date,
                        "commit_message": commit_message
                    })

        return render_template(
            "github_response.html",
            name=github_username,
            repos=repo_details
        )
    else:
        error_message = "Error fetching repositories. \
            Please make sure the GitHub username is valid."
        return render_template(
            "github_response.html",
            name=github_username,
            error_message=error_message)


@app.route("/query", methods=["GET"])
def test_query_return():
    q = request.args.get('q')
    return process_query(q)


def process_query(q):
    if q == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    else:
        return "Unknown"
