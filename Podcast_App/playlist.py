import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pprint

load_dotenv()

# Define user token specific to this application

scopes = 'playlist-modify-public' # Scope to create & modify playlist

username = os.environ.get("SPOTIFY_USER_NAME")
client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")
token = util.prompt_for_user_token(username,
                        scopes,
                        client_id= client_id_saved,
                        client_secret= client_secret_saved,
                        redirect_uri= redirect_uri_saved)


sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials 

#CREATES PLAYLIST

#Get current playlists, will retrieve first 50 (latest)
playlists = sp.current_user_playlists()
playlists_items = playlists['items']
playlists_names = []
for x in playlists_items:
    playlists_names.append(x['name'])
    #IF YOU MAKE TOO MANY PLAYLISTS BY ACCIDENT AND NEED TO DELETE
    #if x['name'] == 'Favorite Podcasts': 
      #  sp.user_playlist_unfollow(username, x['id'])

#Check if "Favorite Podcasts" Playlist exists, if not, create. If it does, print "Favorite Podcasts Exits"

if 'Favorite Podcasts' not in playlists_names:
    playlist = sp.user_playlist_create(username, "Favorite Podcasts", public=True, description='Latest Episodes') #Consider branding app & playlist name
    print(playlist)
else:
    print("Favorite Podcasts Exists")


#ADD NEW EPISODEST TO PLAYLIST

#Revised Spotipy add to playlist function to work with podcast episodes
#Consulted with Gil Cukierman to debug Spotipy code found at this link: https://github.com/plamere/spotipy/blob/24df9ea4cf35248a016b27d9104462e619ca8132/spotipy/client.py#L1482
#Adjustments made:
  # Paramenter "self" to call sp for Spotipy authenticated instance 
  # Paramenter "tracks" changed to "episodes" for continunity
  # ftrack "tracks" swapped for "episode" to create valide URI for Spotify API endpoint

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

#Call add to playlist function to add latest episodes from recent episode URI's list(placeholder list):

recent_ep_uris =['spotify:episode:4iO3CvsdMYlxi39On3AACd', 'spotify:episode:0dl8anyU861xYGgbYn0cop', 'spotify:episode:2SQi1ykYm1CCOu8HprMGnN', 'spotify:episode:1KDoLoOotv3ZluOKgZ36UK']

if not recent_ep_uris:
    updated_playlist = user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None) 
    pprint.pprint(updated_playlist)
else: 
    print("No New Episodes")



