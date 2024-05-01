from flask import Flask, render_template

app = Flask(__name__)

todos = [("Get milk", False), ("Learn programming", True)]

@app.route("/")
def todo():
    return render_template("Jinja_mastery_I.html", todos = todos)
