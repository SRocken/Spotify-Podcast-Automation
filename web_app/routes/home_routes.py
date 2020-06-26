# web_app/routes/home_routes.py

from flask import Blueprint, render_template, request, redirect, flash

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("Welcome to the Spotify Podcast Automation App")
    return render_template("login.html")

@home_routes.route("/activity")
def activity():
    print("Visited Activity Page")
    return render_template("activity.html")