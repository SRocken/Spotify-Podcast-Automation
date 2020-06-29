# Authenticate Spotify Users in order to use the app
# The token and username writing function from this file is used in all other functions throughout the app 
 
import os
import csv

from dotenv import load_dotenv

import spotipy
import spotipy.util as util

load_dotenv()

# Adopted approach to create a token and save the username from https://github.com/gmr50/spotify_app/blob/master/web_app/spotify_methods.py
# Token and username from these functions are then used as params in other primary functions

# Define user token specific to this application

def authenication_token(spotify_username):
    scopes = 'user-library-read user-follow-read playlist-modify-private playlist-modify-public user-read-playback-position' # Scopes set areas the app can access in the authorized user's account - only needs to be authorized once and then is saved in user's preferences
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