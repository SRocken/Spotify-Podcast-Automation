# Functions to in this file contain everything needed to manage the Podify playlist
# Including: check shows followed, checking for new episodes, and adding those episodes
import spotipy
import datetime

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
    first_releases= [item[0] for item in show_items]
    try:
        second_releases= [item[1] for item in show_items]
        recent_releases= first_releases + second_releases
    except IndexError:
        recent_releases= first_releases
    y = datetime.datetime.now()
    today = datetime.date.today()
    yesterday_date= str(today - datetime.timedelta(days=1))
    new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday_date]
    if len(new_release) > 0:
        recent_ep_uris = [sub['id'] for sub in new_release]
        playlists = sp.current_user_playlists()
        playlists_items = playlists['items']
        favorite_podcasts = [x for x in playlists_items if x['name'] == "Podify"]
        playlist = favorite_podcasts[0]
        user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None)
    else:
        print("There are no new episodes to add at this time")