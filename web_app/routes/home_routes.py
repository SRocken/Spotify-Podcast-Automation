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


        # delete user id from csv to maintain clean code
        clear_username_csv()

        write_username_to_csv(username)
        print("Saved username to CSV")

        #auth_url = authenication_token(username).get_authorize_url()#> 'https://accounts.spotify.com/authorize?client_id=_____&response_type=code&redirect_uri=________&scope=playlist-modify-private+playlist-read-private'
        #return redirect(auth_url)

        print("Generating Spotify Token")
        authenication_token(username)
        return redirect("/activity")

    else:
        return render_template("no_token.html")

    app.run(debug=True)

@home_routes.route("/activity")
def activity():
    print("Visited Activity Page")

    username = read_username_from_csv()

    token = authenication_token(username)

    print("Building you a Favorite Podcasts playlist")
    podcast_playlist_generator(username, token)

    print("Adding new episodes for followed podcasts to Favorite Podcasts playlist")
    podcast_followed_new_eps(username, token)

    #print("Printing added episodes:")
    #new_ep_descriptions_titles(username, token)

    print("Emailing you a summary")
    send_episode_email()

    return render_template("activity.html")
