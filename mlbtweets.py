#!/usr/bin/env python3
"""Entry point of Flask app."""
import atexit
import time
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
from models import league, standings

app = Flask(__name__)


@app.route("/home")
def home():
    """Displays the MLB Tweets home page."""
    return render_template("home.html", standings=standings.get())


@app.route("/about")
def about():
    """Displays the MLB Tweets about page."""
    return render_template("about.html", standings=standings.get())


@app.route("/teams/<name>")
def teams(name):
    """Displays the Twitter list page for a given team."""
    team = league.get(name)
    return render_template("team.html", team=team)


scheduler = BackgroundScheduler()
scheduler.add_job(league.update, "cron", day_of_week="wed", hour=4)
scheduler.add_job(standings.update, "cron",  day_of_week="wed", hour=5)


if __name__ == "__main__":
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
    app.run(host="0.0.0.0")
