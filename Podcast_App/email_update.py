import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from sendgrid.helpers.mail import Mail
#from functions_podcast_check import new_ep_descriptions_titles

# import sys
# sys.path.insert(0, Spotify-Podcast-Automation/web_app/spotify_auth.py)
# from spotify_auth import authenication_token  - TODO UPDATE FOR FILE BELOW

load_dotenv()

from web_app.spotify_auth import authenication_token
token = authenication_token(username)
sp = spotipy.Spotify(auth=token)



#MUST REMOVE DUPLICATION
# scopes = 'user-library-read playlist-modify-public' 

# username = os.environ.get("SPOTIFY_USER_NAME")
# client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
# client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
# redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")
# token = util.prompt_for_user_token(username,
#                         scopes,
#                         client_id= client_id_saved,
#                         client_secret= client_secret_saved,
#                         redirect_uri= redirect_uri_saved)

### END OF DUPLICATION

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
TO_EMAIL = os.environ.get("TO_EMAIL")

def send_email(subject="Favorite Podcasts: New Episodes (This is a test)", html="<p>Hello World</p>"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))
    print("SUBJECT:", subject)
    #print("HTML:", html)
    message = Mail(from_email=MY_EMAIL, to_emails=TO_EMAIL, subject=subject, html_content=html)
    try:
        response = client.send(message)
        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    example_html = "TESTING" #new_ep_descriptions_titles(username, token)

    example_subject = "Favorite Podcasts: New Episodes (This is a test)"


    send_email(example_subject, example_html)


    # example_html = f"""
    # <h3>This is a test of the Daily Briefing Service</h3>
    # <h4>Today's Date</h4>
    # <p>Monday, January 1, 2040</p>
    # <h4>My Stocks</h4>
    # <ul>
    #     <li>MSFT | +04%</li>
    #     <li>WORK | +20%</li>
    #     <li>ZM | +44%</li>
    # </ul>
    # <h4>My Forecast</h4>
    # <ul>
    #     <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
    #     <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
    #     <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
    #     <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
    #     <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
    # </ul>
    # """

