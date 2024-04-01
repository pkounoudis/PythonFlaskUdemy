# Flask is a microframework
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/for-loop/")
def render_loops_for():

    planets = {
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    }

    return render_template("for_loops.html", planets = planets)