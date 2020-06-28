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

