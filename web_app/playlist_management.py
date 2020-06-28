# Functions to check episodes from podcasts
import spotipy
import datetime

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

#TODO: Need to make playlist the right definition, right now is just creating a new playlist
        #playlists = sp.current_user_playlists()
        #playlists_items = playlists['items']
        #playlists_names = []
        #for x in playlists_items:
        #    playlists_names.append(x['name'])
        
        playlist = sp.user_playlist_create(username, "Favorite Podcasts", public=True, description='Latest Episodes') #Consider branding app & playlist name
        

        user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None)
    else:
        recent_ep_uris =[]
    
    
    

# TODO: Link to podcast_new_eps and finalize below, ideally plugins should be username, token, recent_ep_uris (from above)

#Revised Spotipy add to playlist function to work with podcast episodes
#Consulted with Gil Cukierman to debug Spotipy code found at this link: https://github.com/plamere/spotipy/blob/24df9ea4cf35248a016b27d9104462e619ca8132/spotipy/client.py#L1482
#Adjustments made:
  # Paramenter "self" to call sp for Spotipy authenticated instance 
  # Paramenter "tracks" changed to "episodes" for continunity
  # ftrack "tracks" swapped for "episode" to create valide URI for Spotify API endpoint

#def add_episodes(username, token, position=None):
#        sp = spotipy.Spotify(auth=token)
#        results = sp.current_user_playlists(limit=50)
#        for i, item in enumerate(results['items']):
#            if i or item["name"] == "Favorite Podcasts":
#                playlist = "Favorite Podcasts"
#                plid = sp._get_id("playlist", playlist_id)
#                ftracks = [sp._get_uri("episode", tid) for tid in episodes]
#                return sp._post(
#                    "users/%s/playlists/%s/tracks" % (username, plid),
#                    payload=ftracks,
#                    position=position,
#                )
#            else:
#                break

##Call add to playlist function to add latest episodes from recent episode URI's list(placeholder list):


#if not recent_ep_uris:
#    updated_playlist = user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None) 
#    pprint.pprint(updated_playlist)
#else: 
#    print("No New Episodes")

