# app/weather_service.py
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import datetime
load_dotenv()


SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
username = os.getenv("username")

scope = 'user-library-read playlist-modify-public'

util.prompt_for_user_token(username,
                           scope,
                           SPOTIPY_CLIENT_ID,
                           SPOTIPY_CLIENT_SECRET,
                           SPOTIPY_REDIRECT_URI)

token = util.prompt_for_user_token(username, scope,cache_path=".cache-" + username )

def user_playlist_add_episodes(
        sp, user, playlist_id, episodes, position=None
    ):
        """ Adds episodes to a playlist
            Parameters:
                - user - the id of the user
                - playlist_id - the id of the playlist
                - episodes - a list of track URIs, URLs or IDs
                - position - the position to add the tracks
        """
        plid = sp._get_id("playlist", playlist_id)
        ftracks = [sp._get_uri("episode", tid) for tid in episodes]
        return sp._post(
            "users/%s/playlists/%s/tracks" % (user, plid),
            payload=ftracks,
            position=position,
        )



sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_shows()
items = results["items"]
ID_LIST = [p["show"]["id"] for p in items]
episodes = []
for x in ID_LIST:
    sodes = sp.show(x)
    episodes.append(sodes) 
show_items = [p["episodes"]["items"] for p in episodes]
recent_releases = [item[0] for item in show_items]
y = datetime.datetime.now()
date_today = str(y.strftime("%Y-%m-%d"))
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))
new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday or date_today]
playlist = "6Rl3mWSHnsZ8CRjHRs4NCq"
if len(new_release) > 0:
    recent_ep_uris = [ sub['id'] for sub in new_release] 
    #print(recent_ep_uris)
    updated_playlist = user_playlist_add_episodes(sp, username, playlist, recent_ep_uris, position=None) 
    print("DONE")
else: 
    print("NONE")
    exit()
