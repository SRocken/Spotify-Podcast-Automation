# Functions to check episodes from podcasts
import spotipy
import datetime

from spotify_auth import authenication_token, read_username_from_csv

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
    today = datetime.date.today()
    yesterday = str(today - datetime.timedelta(days=1))
    new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday]
   
    if len(new_release) > 0:
        recent_ep_uris = [sub['id'] for sub in new_release]
        playlists = sp.current_user_playlists()
        playlists_items = playlists['items']
        favorite_podcasts = [x for x in playlists_items if x['name'] == "Favorite Podcasts"]
        playlist = favorite_podcasts[0]
        user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None)
    else:
        print("There are no new episodes to add at this time")

def new_ep_descriptions_titles(username, token):
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
        recent_ep_uris = [sub['uri'] for sub in new_release] 
        new_episodes = []
        for x in recent_ep_uris:
            sodes = sp.episode(x)
            new_episodes.append(sodes)
        #episode_info = ["PODCAST: " + q['show']["name"] + "\n" + "EPISODE: " + q['name'] + "\n"  + "DESCRIPTION: " + q['description'] +  "\n" + "LINK: " + q['external_urls']['spotify'] for q in new_episodes]        
        episode_info = [{"show": q['show']["name"], "name": q['name']} for q in new_episodes]
        return episode_info
    else:
        episode_info = {
            "show": "No new episodes have been added",
            "name": ""
        }
        return episode_info
        # Need this return "No new episodes" in a way that works with the email


#if __name__ == "__main__":
#    username = read_username_from_csv()
#    token = authenication_token(username)
#
#    #Add new episodes to Favorite Podcasts list
#    #podcast_followed_new_eps(username, token)
#
#    #Pulling together episode descriptions for each added episode
#    print(new_ep_descriptions_titles(username, token))