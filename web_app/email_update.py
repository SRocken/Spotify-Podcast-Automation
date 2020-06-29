# This file contains the app that updates the Favorite Podcast Playlist with the latest episodes
# and then sends the user an email summary of what was added
# send_episode_email is called in the Flask App to send an email whenever the Flask app is used 

import os
import datetime
import spotipy

from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

# Send email using template function
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
    recent_releases = [item[0] for item in show_items]
    y = datetime.datetime.now()
    date_today = str(y.strftime("%Y-%m-%d"))
    today = datetime.date.today()
    yesterday = str(today - datetime.timedelta(days=1))
    new_release = [b for b in recent_releases if str(b["release_date"]) == yesterday] #or date_today]
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
        episode_details = [{"show":"Sorry", "name": "There are no new episodes to add to your playlist"}]

    # Sendgrid template data
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

#Need to run web app at least once before using this as main app
if __name__ == "__main__":
    from spotify_auth import authenication_token, read_username_from_csv
    from playlist_management import podcast_followed_new_eps
  
    username = read_username_from_csv()
    token = authenication_token(username)

    # Add new episodes to Favorite Podcasts list
    podcast_followed_new_eps(username, token)

    # Send email
    send_episode_email(username, token)


