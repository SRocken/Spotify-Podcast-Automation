# web_app/routes/home_routes.py

from flask import Blueprint, render_template, request, redirect, flash

from web_app.spotify_auth import authenication_token, write_username_to_csv, read_username_from_csv, clear_username_csv
from web_app.playlist_creator import podcast_playlist_generator
from web_app.playlist_management import podcast_followed_new_eps
from web_app.email_update import send_episode_email

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("Welcome to the Spotify Podcast Automation App")
    return render_template("login.html")


@home_routes.route("/create/", methods = ['GET', 'POST'])
def Execute(username=None):
    print("Executing login script")

    username = request.args["username"]

    username_detected = False

    if(username):
        username_detected = True

    if(username_detected):
        print("debug: " + username)
        print("username detected")

        # Delete user id from csv to maintain clean code
        clear_username_csv()

        write_username_to_csv(username)
        print("Saved username to CSV")

        print("Generating Spotify Token")
        authenication_token(username)
        return redirect("/activity")

    else:
        return render_template("no_token.html")

    app.run(debug=True)

# Functions being pulled from other .py files in the repo to run all the features of the application neatly
# On this page of the Flask app, the Podify playlist is created if it does not already exist
# Then the application checks which Podcast shows the user follows, and pulls the new episodes (date = yesterday only) from that show to add to the playlist
# Finally, an email is sent to the user with a summary of the shows added 
@home_routes.route("/activity")
def activity():
    print("Visited Activity Page")

    username = read_username_from_csv()

    token = authenication_token(username)

    print("Building you a Podify playlist")
    podcast_playlist_generator(username, token)

    print("Adding new episodes for followed podcasts to Podify playlist")
    podcast_followed_new_eps(username, token)

    print("Emailing you a summary")
    send_episode_email(username, token)

    return render_template("activity.html")
