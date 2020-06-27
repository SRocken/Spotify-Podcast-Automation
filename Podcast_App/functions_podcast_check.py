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

#Get Followed Show IDS
for i in SHOW_LIST:
    ID_LIST = [i["id"] for i in SHOW_LIST]

#Compile episodes of Followed Shows
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
for q in episodes:
    episode_in = [q['episodes'] for q in episodes]
for q in episode_in:
    show_items = [q['items'] for q in episode_in]

#Get Most Recent 
recent_releases = [item[0] for item in show_items]
recent_ep_uris = [ sub['uri'] for sub in recent_releases ] 
recent_descriptions = [ sub['description'] for sub in recent_releases ] 
recent_show_titles= [ sub['description'] for sub in recent_releases ] 

#print(*recent_descriptions, sep='\n')

#print(episodes)

# Get Descriptions 


#FULL META DATA FOR NEW EPS

def new_podcast_(username, token):
    sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        if i or item["name"] != "Favorite Podcasts":
            sp.user_playlist_create(username, "Favorite Podcasts", public=True, description='Latest Episodes') #Consider branding app & playlist name
        else:
            break

new_episodes = []
for x in recent_ep_uris:
    sodes = sp.episode(x)
    new_episodes.append(sodes)
print(new_episodes)


#EPISODE TITLE and Description List 
for q in new_episodes:
    episode_info = str([q['name'] + q['description'] for q in new_episodes])
#print(episode_info)

#print(episode_info)


