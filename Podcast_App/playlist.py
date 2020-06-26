import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json

load_dotenv()
# Define user token specific to this application

scopes = 'playlist-modify-public' # Scope to create playlist

username = os.environ.get("SPOTIFY_USER_NAME")
client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")
token = util.prompt_for_user_token(username,
                        scopes,
                        client_id= client_id_saved,
                        client_secret= client_secret_saved,
                        redirect_uri= redirect_uri_saved)


sp = spotipy.Spotify(auth=token) #calls spotipy wiht authorized credentials 

sp.user_playlist_create(username, "Favorite Podcasts", public=True, description='Latest Episodes') #Consider branding app & playlist name
