import os
from dotenv import load_dotenv
import spotipy
import sys #TODO: TAKE OUT
from spotipy.oauth2 import SpotifyClientCredentials #TODO: TAKE OUT
import spotipy.util as util #TODO: TAKE OUT
import datetime #TODO: TAKE OUT
from sendgrid import SendGridAPIClient #TODO: TAKE OUT
from sendgrid.helpers.mail import Mail #TODO: TAKE OUT
from playlist_creator import podcast_playlist_generator
from playlist_management import podcast_followed_new_eps, new_ep_descriptions_titles, user_playlist_add_episodes
from email_update import send_episode_email 

load_dotenv() #TODO: TAKE OUT

#TODO: REPLACE WITH FUNCTION FROM SPOTIFY_AUTH.PY (see below)
# add above: from spotify_auth import authenication_token
# add this below the username variable: authenication_token(username)
client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID") #TODO: TAKE OUT
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET") #TODO: TAKE OUT
redirect_uri_saved = os.environ.get("SPOTIPY_REDIRECT_URI") #TODO: TAKE OUT
username = os.getenv("USERNAME")
scope = 'user-library-read playlist-modify-public' #TODO: TAKE OUT

util.prompt_for_user_token(username,#TODO: TAKE OUT
                        scope,#TODO: TAKE OUT
                        client_id= client_id_saved,#TODO: TAKE OUT
                        client_secret= client_secret_saved,#TODO: TAKE OUT
                        redirect_uri= redirect_uri_saved)#TODO: TAKE OUT

token = util.prompt_for_user_token(username, scope)#TODO: TAKE OUT

sp = spotipy.Spotify(auth=token)


podcast_playlist_generator(username, token) #TODO: TAKE OUT
podcast_followed_new_eps(username, token)
new_ep_descriptions_titles(username, token) #TODO: TAKE OUT
send_episode_email(username, token)