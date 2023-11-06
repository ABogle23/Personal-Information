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
@app.route("/")
def github_username():
    return render_template("github.html")


#github
@app.route("/submit_github", methods=["POST"])
def submit_github():
    input_name = request.form.get("name")
    return render_template(
        "github_response.html",
        name=input_name
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
