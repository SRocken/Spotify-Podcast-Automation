import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import datetime

#from spotify_auth import authenication_token, read_username_from_csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()
client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")
username = os.getenv("username")
scope = 'user-library-read playlist-modify-public'
#
util.prompt_for_user_token(username,
                        scope,
                        client_id= client_id_saved,
                        client_secret= client_secret_saved,
                        redirect_uri= redirect_uri_saved)

token = util.prompt_for_user_token(username, scope)

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
    

def run_full(username, token):
    sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials
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
    second_releases= [item[1] for item in show_items]
    recent_releases= first_releases + second_releases
    y = datetime.datetime.now()
    today = datetime.date.today()
    date_today = str(y.strftime("%Y-%m-%d"))#https://docs.python.org/3/library/datetime.html
    yesterday_date= str(today - datetime.timedelta(days=1)) #https://stackoverflow.com/questions/1712116/formatting-yesterdays-date-in-python
    new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday_date]
    if len(new_release) > 0:
        recent_ep_uris = [sub['id'] for sub in new_release]
        playlists = sp.current_user_playlists()
        playlists_items = playlists['items']
        favorite_podcasts = [x for x in playlists_items if x['name'] == "Favorite Podcasts"]
        playlist = favorite_podcasts[0]
        user_playlist_add_episodes(sp, username, playlist['id'], recent_ep_uris, position=None)
        print("done")
    else:
        print("There are no new episodes to add at this time")
    
run_full(username, token)

def send_episode_email(username, token):
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
    second_releases= [item[1] for item in show_items]
    recent_releases= first_releases + second_releases
    y = datetime.datetime.now()
    date_today = str(y.strftime("%Y-%m-%d"))#https://docs.python.org/3/library/datetime.html
    today = datetime.date.today()
    yesterday_date = str(today - datetime.timedelta(days=1)) #https://stackoverflow.com/questions/1712116/formatting-yesterdays-date-in-python
    new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday_date]
    if len(new_release) > 0:
        recent_ep_uris = [sub['uri'] for sub in new_release] 
        new_episodes = []
        for x in recent_ep_uris:
            sodes = sp.episode(x)
            new_episodes.append(sodes)
        episode_details = [{
            "show": q['show']["name"],
            "name": q['name']}
            for q in new_episodes
        ]
    else:
        episode_details = {
            "show": "No new episodes have been added",
            "name": ""
        }

    template_data = {"episode_info": episode_details}
 
    # Building the ability to send the email
    client = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
    
    message = Mail(from_email=os.environ.get("MY_EMAIL"),to_emails=os.environ.get("TO_EMAIL"))
     
    message.template_id = os.environ.get("SENDGRID_TEMPLATE_ID")

    message.dynamic_template_data = template_data    
    
    try:
        response = client.send(message)
        print("RESPONSE: ", type(response))
        print(response.status_code) # if 202 prints then SUCCESS
        print(response.body)
        print(response.headers)
        return response
    except Exception as e:
        print(e)
        return None

#Need to run web app at least once before using this
#from spotify_auth import authenication_token, read_username_from_csv
#token = authenication_token(username)
send_episode_email(username, token)


