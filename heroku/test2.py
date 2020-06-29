# app/weather_service.py
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import utils as util
import datetime
load_dotenv()


#
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
username = os.getenv("username")
scope = 'user-library-read playlist-modify-public'
#
util.prompt_for_user_token(username,
                           scope,
                           SPOTIPY_CLIENT_ID,
                           SPOTIPY_CLIENT_SECRET,
                           SPOTIPY_REDIRECT_URI)

token = util.prompt_for_user_token(username, scope)



from spotify_auth import authenication_token, read_username_from_csv
from playlist_management import podcast_followed_new_eps
from email_update import send_episode_email

username = read_username_from_csv()
token = authenication_token(username)
#Add new episodes to Favorite Podcasts list
podcast_followed_new_eps(username, token)
#Send email
send_episode_email(username, token)


