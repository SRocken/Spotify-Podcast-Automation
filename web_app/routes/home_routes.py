# web_app/routes/home_routes.py

from flask import Blueprint, render_template, request, redirect, flash

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("Welcome to the Spotify Podcast Automation App")
    return render_template("login.html")


@home_routes.route("/create", methods = ['GET', 'POST'])
def Execute(username=None):
    print("Executing login script")

    username = request.args["username"]

    username_detected = False

    if(username):
        username_detected = True

    if(username_detected):
        print("debug: " + username)
        print("username detected")
        #session['username'] = username

        write_username_to_csv(username)

        print("saved to memory")

        auth_url = authenication_token(username).get_authorize_url()#> 'https://accounts.spotify.com/authorize?client_id=_____&response_type=code&redirect_uri=________&scope=playlist-modify-private+playlist-read-private'
        print("redirect")
        return redirect(auth_url)
    else:
        return render_template("no_token.html")

    app.run(debug=True)

@home_routes.route("/callback/")
def Callback(code=None):

    print("callback")
    spotify_username = read_username_from_csv()

    #delete user id from csv to maintain clean code
    clear_username_csv()

    #changed flow to accommodate changes of domain, resets session variable with expectation session will persist
    session['username'] = spotify_username

    print("get user id from csv")
    print(spotify_username)

    #gets authorization code from url
    print("SPOTIFY CALLBACK")
    print("REQUEST PARAMS:", dict(request.args))

    if "code" in request.args:
        code = request.args["code"]
        print("CODE:", code)

        sp_oauth = authenication_token(spotify_username)
        token_info = sp_oauth.get_access_token(code)
        print("TOKEN INFO:", token_info)
        token = token_info["access_token"]
        print("ACCESS TOKEN:", token)

        session['token_var'] = token

        check = check_login(token, spotify_username)
        if(check):
            print("Taking you to your podcast activity page")
            return redirect("/activity")
        else:
            return render_template("no_token.html")
    else:
        message = "OOPS, UNABLE TO GET CODE"
        print(message)
        return message


@home_routes.route("/activity")
def activity():
    print("Visited Activity Page")
    return render_template("activity.html")