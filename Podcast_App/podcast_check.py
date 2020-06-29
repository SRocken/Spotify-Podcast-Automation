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
import datetime

# Date 

y = datetime.datetime.now()
date_today = str(y.strftime("%Y-%m-%d"))
today = datetime.date.today()
yesterday = str(today - datetime.timedelta(days=1))

print(yesterday)
print(date_today)



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
new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday or date_today]
recent_ep_uris = [ sub['id'] for sub in new_release] 
recent_descriptions = [ sub['description'] for sub in recent_releases ] 
recent_show_titles= [ sub['description'] for sub in recent_releases ] 
episode_dates = [ sub['release_date'] for sub in recent_releases ] 
print(recent_ep_uris)

#newly_released_list = []
#new_release = [b for b in recent_releases if str(b["release_date"]) == "2020-06-27" or "2020-06-27"]
#newly_released_list.append(new_release)
#print(recent_releases)
#print(new_release)
#print(episode_dates)

#print(newly_released_list)

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


