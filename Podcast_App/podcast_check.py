# app/weather_service.py
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
load_dotenv()
import requests
import datetime

# Date 

y = datetime.datetime.now()
date_today = (y.strftime("%Y-%m-%d"))

today = datetime.date.today()

yesterday = str(today - datetime.timedelta(days=1))

print(yesterday)

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


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_shows()
    items = results["items"]
    #print(items)
else:
    print("Can't get token for", username)

#print(results)
# 'spotify:show:5fRBo7ROBQNq8IAavbO64H'


show_id = "spotify:show:5fRBo7ROBQNq8IAavbO64H"

for p in items:
    SHOW_LIST = [p["show"] for p in items]
    #print(SHOW_LIST)

for i in SHOW_LIST:
    ID_LIST = [i["id"] for i in SHOW_LIST]

print(ID_LIST)
episodes = []

for x in ID_LIST:
    sodes = sp.show(x)
    episodes.append(sodes)
#print(episodes)


#Podcast Desdcription 
for q in episodes:
    episode_info = [q['description'] for q in episodes]
    #print(episode_info)


for q in episodes:
    episode_in = [q['episodes'] for q in episodes]
    #print(episode_in[0])

for q in episode_in:
    show_items = [q['items'] for q in episode_in]
#print(show_items[])

first = show_items[0]
second = show_items[1]

released_list = []

for b in show_items:
    releases = selected_pods = [b for b in first if str(b["release_date"]) == yesterday]
    released_list.append(releases)

print(released_list)
#print(getList(first)) 

#print(first)



#for b in first:
#    selected_pods = [b for b in first if str(b["release_date"]) == yesterday]
#
uri_list = []


#for d in released_list:
#    new_episode = [d["uri"] for d in released_list]
#    uri_list.append(new_episode)
#
uris = uri_list



#print(new_episode)

