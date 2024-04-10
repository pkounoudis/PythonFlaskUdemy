# Flask is a microframework
from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def _init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/") # The "/" is an endpoint
def data_structures():
    
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {"movies": movies,
            "car": car,
            "moons": moons}

    return render_template(
    "data_structures.html", **kwargs) # Objects to be interpolated
