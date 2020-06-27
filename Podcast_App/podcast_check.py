# app/weather_service.py
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
load_dotenv()
import requests
import datetime

# Date 



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


ID_LIST = [p["show"]["id"] for p in items]
episodes = []
for x in ID_LIST:
    sodes = sp.show(x)
    episodes.append(sodes)


#recent_ep_uri = [ sub['uri'] for sub in recent_releases ] 

#Podcast Desdcription 
#for q in episodes:
#    episode_info = [q['description'] for q in episodes]
#    #print(episode_info)


#Remove Show Meta Data


show_items = [p["episodes"]["items"] for p in episodes]
#Get Most Recent 
recent_releases = [item[0] for item in show_items]
recent_ep_uris = [ sub['uri'] for sub in recent_releases ] 
recent_descriptions = [ sub['description'] for sub in recent_releases ] 
recent_show_titles= [ sub['description'] for sub in recent_releases ] 
print(recent_ep_uris)

#print(*recent_descriptions, sep='\n')

#print(episodes)

# Get Descriptions 


#FULL META DATA FOR NEW EPS



new_episodes = []
for x in recent_ep_uris:
    sodes = sp.episode(x)
    new_episodes.append(sodes)
#print(new_episodes)


#EPISODE TITLE and Description List 
for q in new_episodes:
    episode_info = [q['show']["name"] + ":" + " " + q['name'] + " " + q['description'] for q in new_episodes]
    #show_titles = str([q['show']["name"] for q in new_episodes])
#print(show_titles)
#print(*episode_info, sep = "\n")


