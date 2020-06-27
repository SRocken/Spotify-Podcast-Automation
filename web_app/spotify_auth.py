# Authenticate Spotify Users in order to use the app 
 
import os

from dotenv import load_dotenv

import spotipy
import spotipy.util as util

load_dotenv()

# Define user token specific to this application

def authenication_token(spotify_username):
    scopes = 'user-follow-read playlist-modify-private user-read-playback-position' # Scopes set areas the app can access in the authorized user's account - only needs to be authorized once and then is saved in user's preferences
    username = input("Please input your username: ") #TODO: Make this part of the flask web app

    client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")

    token = util.prompt_for_user_token(username,
                            scopes,
                            client_id= client_id_saved,
                            client_secret= client_secret_saved,
                            redirect_uri= redirect_uri_saved)
    
    return token