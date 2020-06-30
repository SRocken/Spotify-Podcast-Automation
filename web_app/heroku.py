import os
from dotenv import load_dotenv

import spotipy
import spotipy.util as util
from spotify_auth import authenication_token, read_username_from_csv
from playlist_creator import podcast_playlist_generator
from playlist_management import podcast_followed_new_eps, user_playlist_add_episodes
from email_update import send_episode_email

load_dotenv()


username = read_username_from_csv()

token = authenication_token(username)

sp = spotipy.Spotify(auth=token)

podcast_playlist_generator(username, token)

podcast_followed_new_eps(username, token)

send_episode_email(username, token)