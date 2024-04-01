# Flask is a microframework
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/conditionals-basics/")
def render_conditionals():
    company = "Apple"
    return render_template("conditional_basics.html", company = company)