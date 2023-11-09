import requests
import os
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__)
load_dotenv()


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


@app.route("/twitter_test")
def twitter_test():
    access_token = os.getenv("access_token")
    access_token_secret = os.getenv("access_token_secret")
    api_key = os.getenv("api_key")
    api_key_secret = os.getenv("api_key_secret")

    url = 'https://api.twitter.com/2/users/me'
    auth = OAuth1(api_key, api_key_secret, access_token, access_token_secret)

    request_response = requests.get(url, auth=auth)
    print(request_response.json())

    return render_template("twitter_test.html")


@app.route("/github")
def github():
    return render_template("github.html")


@app.route("/submit_github", methods=["POST"])
def submit_github():
    github_username = request.form.get("github_username")

    # Get information about the user's repositories and thus commits

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

        socials_response = requests.get(
            f"https://api.github.com/users/{github_username}/social_accounts",
            timeout=10)

        if socials_response.status_code == 200:
            socials = socials_response.json()
            if socials:
                first_social_url = socials[0]["url"].split("/")[-1]
            else:
                msg = "there is no social account \
                    associated with this github account"
                first_social_url = msg
        else:
            msg = "there is no social account \
                associated with this github account"
            first_social_url = msg

        return render_template(
            "github_response.html",
            name=github_username,
            repos=repo_details,
            social_url=first_social_url)

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
