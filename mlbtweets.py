#!/usr/bin/env python3
"""Entry point of Flask app."""
from flask import Flask, render_template
from models import league

app = Flask(__name__)


@app.route("/home")
def home():
    """Displays the MLB Tweets home page."""
    return render_template("home.html")


@app.route("/about")
def about():
    """Displays the MLB Tweets about page."""
    return render_template("about.html")


@app.route("/teams/<name>")
def teams(name):
    """Displays the Twitter list page for a given team."""
    team = league.get(name)
    return render_template("team.html", team=team)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
