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

token = util.prompt_for_user_token(username, scope)






def podcast_followed_new_eps(username, token):
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
    if len(new_release) > 0:
        recent_ep_uris = [ sub['id'] for sub in new_release] 
        print(recent_ep_uris)
    else:
        recent_ep_uris =[]
        #print(recent_ep_uris)


#podcast_followed_new_eps(username, token)

print('--------')

def new_ep_descriptions_titles(username, token):
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
    if len(new_release) > 0:
        recent_ep_uris = [ sub['uri'] for sub in new_release] 
        new_episodes = []
        for x in recent_ep_uris:
            sodes = sp.episode(x)
            new_episodes.append(sodes)
        episode_info = ["PODCAST: " + q['show']["name"] + "\n" + "EPISODE: " + q['name'] + "\n"  + "DESCRIPTION: " + q['description'] +  "\n" + "LINK: " + q['external_urls']['spotify'] for q in new_episodes]
        #print(*episode_info, sep = "\n" + "\n" + "\n")
        print(*episode_info, sep = "\n" + "\n" + "\n" + "\n")
    else:
        episode_info = []

#new_ep_descriptions_titles(username, token)


# IMAGE FUNCTION WORK IN PROGRESS 
def new_ep_image_urls(username, token):
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
    if len(new_release) == 0:
        recent_ep_uris =[]
        exit()
    recent_ep_uris = [ sub['uri'] for sub in new_release] 
    new_episodes = []
    for x in recent_ep_uris:
        sodes = sp.episode(x)
        new_episodes.append(sodes)
    episode_images_details = [q['images'] for q in new_episodes]
    #print(episode_images_details)
    single_urls = [b for b in episode_images_details if str(b["height"]) == "640"]
    print(single_urls)
#new_ep_image_urls(username, token)