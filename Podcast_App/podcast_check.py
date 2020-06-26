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

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SPOTIPY_REDIRECT_URI = os.getenv("username")
import sys
import spotipy
import spotipy.util as util



scope = 'user-library-read playlist-modify-public'

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



for p in items:
    SHOW_LIST = [p["show"] for p in items]
    #print(SHOW_LIST)


for i in SHOW_LIST:
    ID_LIST = [i["id"] for i in SHOW_LIST]
#print(ID_LIST)

#artist_albums(artist_id, album_type=None, country=None, limit=20, offset=0)

#joined_id_list = " ".join(ID_LIST)

#GET https://api.spotify.com/v1/shows/{id}/episodes
#spotify_id = 

#episode_list = sp.artist.tracks(ID_LIST)
#items = results["items"]

#GET f"https://api.spotify.com/v1/shows/{x}/episodes"

x = "5fRBo7ROBQNq8IAavbO64H"

#request_url = f"https://api.spotify.com/v1/shows/{x}/episodes"
#episodes = requests.get(request_url)
#parsed_response = json.loads(episodes.text)
#episode_list = sp.show(x)
#print(parsed_response)

#print(episode_list)

episodes = []

for x in ID_LIST:
    sodes = sp.show(x)
    episodes.append(sodes)
print(episodes)

#print
    #print(items)
#id_number = p['id']

#show_details = items["show"]

#print(show_details)


#p = items[0]
#id_number = p['id']

#print(id_number)

#date_list = []
#


#for x in items:
#    show = [p for p in items if str(p["show"]) == "show"]
    
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



#{'href': 'https://api.spotify.com/v1/me/shows?offset=0&limit=50', 

#'items': [{'added_at': '2020-06-26T02:27:26Z', 'show': {'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'copyrights': [], 'description': '       The podcast about chain restaurants. Comedians Mike Mitchell and Nick Wiger review fast food/sit-down chains and generally argue about food/everything.     ', 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/show/5fRBo7ROBQNq8IAavbO64H'}, 'href': 'https://api.spotify.com/v1/shows/5fRBo7ROBQNq8IAavbO64H', 'id': '5fRBo7ROBQNq8IAavbO64H', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/95b9536af2e3854c496270ca2603f62350d8db6a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/3247c54c730c2fef713aa6cabacae88038da84ab', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/579ce238f3ac0dc14d0cc13e1a9c2ec6b0a399ba', 'width': 64}], 'is_externally_hosted': False, 'languages': ['en'], 'media_type': 'audio', 'name': 'Doughboys', 'publisher': 'HeadGum / Doughboys Media', 'type': 'show', 'uri': 'spotify:show:5fRBo7ROBQNq8IAavbO64H'}}], 'limit': 50, 'next': None, 'offset': 0, 'previous': None, 'total': 1}
