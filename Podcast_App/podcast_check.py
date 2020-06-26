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

import sys
import spotipy
import spotipy.util as util



scope = 'user-library-read playlist-modify-public'
username = "chefbrahardee"
util.prompt_for_user_token(username,
                           scope,
                           SPOTIPY_CLIENT_ID,
                           SPOTIPY_CLIENT_SECRET,
                           SPOTIPY_REDIRECT_URI)




token = util.prompt_for_user_token(username, scope)

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_shows()
    items = results["items"]
    #print(items)
else:
    print("Can't get token for", username)

p = items[0]
print(p["added_at"])

#date_list = []
#
#for x in items:
#    date = [p for p in results if str(p["show"]) == "show"]
#    date_list.append(date)
#    print(date_list)
#    

#print(date)

#product_list = [str(p["id"]) for p in products]

#name_list = [str(p["id"]) for p in products]
#name = [p for p in items if (p["href"]) == "href"]




# 'https://api.spotify.com/v1/me/shows?offset=0&limit=50


#print saved shows 
#if token:
#    sp = spotipy.Spotify(auth=token)
#    results = sp.current_user_saved_shows()
#    print(results["name"])
#else:
#    print("Can't get token for", username)
#
#def show_tracks(tracks):
#    for i, item in enumerate(tracks['items']):
#        track = item['track']
#        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
#            track['name']))
#
#
#if __name__ == '__main__':
#    if len(sys.argv) > 1:
#        username = "chefbrahardee"
#    else:
#        print("Whoops, need your username!")
#        print("usage: python user_playlists.py [username]")
#        sys.exit()
#
#    token = util.prompt_for_user_token(username)
#
#    if token:
#        sp = spotipy.Spotify(auth=token)
#        playlists = sp.user_playlists(username)
#        for playlist in playlists['items']:
#            if playlist['owner']['id'] == username:
#                print()
#                print(playlist['name'])
#                print ('  total tracks', playlist['tracks']['total'])
#                results = sp.playlist(playlist['id'],
#                    fields="tracks,next")
#                tracks = results['tracks']
#                show_tracks(tracks)
#                while tracks['next']:
#                    tracks = sp.next(tracks)
#                    show_tracks(tracks)
#    else:
#        print("Can't get token for", username)