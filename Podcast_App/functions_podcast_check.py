# app/weather_service.py
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

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

token = util.prompt_for_user_token(username, scope)






def podcast_followed_new_eps(username, token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_shows()
    items = results["items"]
    for p in items:
        SHOW_LIST = [p["show"] for p in items]
    for i in SHOW_LIST:
        ID_LIST = [i["id"] for i in SHOW_LIST]
    episodes = []
    for x in ID_LIST:
        sodes = sp.show(x)
        episodes.append(sodes)
    for q in episodes:
        episode_in = [q['episodes'] for q in episodes]
    for q in episode_in:
        show_items = [q['items'] for q in episode_in]
    recent_releases = [item[0] for item in show_items]
    recent_ep_uris = [ sub['uri'] for sub in recent_releases ] 
    recent_descriptions = [ sub['description'] for sub in recent_releases ] 
    recent_show_titles= [ sub['description'] for sub in recent_releases ] 
    new_episodes = []
    for x in recent_ep_uris:
        sodes = sp.episode(x)
        new_episodes.append(sodes)
    #print(new_episodes)
    for q in new_episodes:
        episode_info = str([q['name'] + q['description'] for q in new_episodes])
    print(recent_ep_uris)


podcast_followed_new_eps(username, token)

def new_ep_descriptions_titles(username, token):
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_shows()
    items = results["items"]
    for p in items:
        SHOW_LIST = [p["show"] for p in items]
    for i in SHOW_LIST:
        ID_LIST = [i["id"] for i in SHOW_LIST]
    episodes = []
    for x in ID_LIST:
        sodes = sp.show(x)
        episodes.append(sodes)
    for q in episodes:
        episode_in = [q['episodes'] for q in episodes]
    for q in episode_in:
        show_items = [q['items'] for q in episode_in]
    recent_releases = [item[0] for item in show_items]
    recent_ep_uris = [ sub['uri'] for sub in recent_releases ] 
    recent_descriptions = [ sub['description'] for sub in recent_releases ] 
    recent_show_titles= [ sub['description'] for sub in recent_releases ] 
    new_episodes = []
    for x in recent_ep_uris:
        sodes = sp.episode(x)
        new_episodes.append(sodes)
    #print(new_episodes)
    for q in new_episodes:
    episode_info = [q['show']["name"] + ":" + " " + q['name'] + " " + q['description'] for q in new_episodes]
    print(*episode_info, sep = "\n")

