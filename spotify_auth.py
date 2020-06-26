# Authenticate Spotify Users in order to use the app

import os
import sys

from dotenv import load_dotenv

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

load_dotenv()

scope = 'user-library-read' # Scope sets access for the app in the authorized user's account
username = input("Please input your username: ")

client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")

token = util.prompt_for_user_token(username,
                        scope,
                        client_id= client_id_saved,
                        client_secret= client_secret_saved,
                        redirect_uri= redirect_uri_saved)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)