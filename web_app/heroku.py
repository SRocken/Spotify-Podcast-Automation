import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util
from playlist_creator import podcast_playlist_generator
from playlist_management import podcast_followed_new_eps, new_ep_descriptions_titles, user_playlist_add_episodes
from email_update import send_episode_email

load_dotenv()
client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri_saved = os.environ.get("SPOTIPY_REDIRECT_URI")
username = os.getenv("username")
scope = 'user-library-read playlist-modify-public'

util.prompt_for_user_token(username,
                        scope,
                        client_id= client_id_saved,
                        client_secret= client_secret_saved,
                        redirect_uri= redirect_uri_saved)

token = util.prompt_for_user_token(username, scope)
sp = spotipy.Spotify(auth=token)


podcast_playlist_generator(username, token)
podcast_followed_new_eps(username, token)
new_ep_descriptions_titles(username, token)
send_episode_email(username, token)