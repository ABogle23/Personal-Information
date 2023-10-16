from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
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
	elif surface = "Off-Road":
		bicycle_recommendation == "Mountain Bike"

    return render_template("hello.html", name=input_name, age=input_age, surface=surface, activity=activity, storage=storage, bicycle_recommendation=bicycle_recommendation)
