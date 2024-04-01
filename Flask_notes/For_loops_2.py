# Flask is a microframework
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/for-loop/")
def render_for_loops_conds():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }

    render_template("for_loops_2.html", user_os = user_os )