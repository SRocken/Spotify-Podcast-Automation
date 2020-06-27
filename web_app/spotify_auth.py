# Authenticate Spotify Users in order to use the app 
 
import os
import csv

from dotenv import load_dotenv

import spotipy
import spotipy.util as util

load_dotenv()

# Define user token specific to this application

def authenication_token(spotify_username):
    scopes = 'user-follow-read playlist-modify-private playlist-modify-public user-read-playback-position' # Scopes set areas the app can access in the authorized user's account - only needs to be authorized once and then is saved in user's preferences
    username = spotify_username 

    client_id_saved = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret_saved = os.environ.get("SPOTIFY_CLIENT_SECRET")
    redirect_uri_saved = os.environ.get("SPOTIFY_REDIRECT_URI")

    token = util.prompt_for_user_token(username,
                            scopes,
                            client_id= client_id_saved,
                            client_secret= client_secret_saved,
                            redirect_uri= redirect_uri_saved)
    
    return token

def write_username_to_csv(username):
    csv_filepath = os.path.normpath(os.getcwd()) + "/web_app/username.csv"

    try:
        with open(csv_filepath, "w") as csv_file: # "w" means "open the file for writing"
            writer = csv.writer(csv_file)
            writer.writerow([str(username)])

    except:
        print("No csv file to write to")

    success = True

    return success

def read_username_from_csv():
    csv_filepath = os.path.normpath(os.getcwd()) + "/web_app/username.csv"
    with open(csv_filepath, "r") as csv_file: # "r" means read csv file
        reader = csv.reader(csv_file)
        row1 = next(reader)
        #for row in reader:
            #print("Updating saved username")
            #username = str(row)
            #username = username[2:-2]
        print("Reading saved username:")
        username = row1
        username = "".join(username)
        print(username)

    return username

def clear_username_csv():
    
    print("Clearing saved usernames")
    csv_filepath = os.path.normpath(os.getcwd()) + "/web_app/username.csv"
    csv = open(csv_filepath, "w")
    csv.truncate()
    csv.close()

    cleared = True

    return cleared

def check_login(token,spotify_username):
    sp = spotipy.Spotify(auth=token)

    me = sp.current_user()

    if(me['id'] != spotify_username):
        return False
    else:
        return True
