from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

# Wrap the functionalitites in a create_app() function, to avoid problems | Factory Pattern.
def create_app():
    
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://Panos_Kounoudis:iYJmnq5QeTipkM7r@cluster0.z0ghwkx.mongodb.net/")
    app.db = client.microblog

    # entries = [] We do not need that list anymore, we have MongoDB!

    @app.route("/", methods=["GET", "POST"])
    def home():
        # print([e for e in app.db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            # entries.append((entry_content, formatted_date)) We do not need that list anymore, we have MongoDB!

            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        #Datetime implementation
        entries_with_date = [
            (
            entry["content"], 
            entry["date"], 
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            
            for entry in app.db.entries.find({})
        ]

        return render_template("home.html", entries = entries_with_date)
    
    return app

