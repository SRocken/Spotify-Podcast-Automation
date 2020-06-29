import spotipy
import spotipy.util as util
import json
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import datetime
load_dotenv()
import requests
from flask import Flask, render_template, redirect, request, session, make_response,session,redirect
#
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
username = os.getenv("username")
cache_path = {"access_token": "BQCjPUOPvrT2MFb2hj3OXVSbfUO5ijRh30fCs_4EwCX-4D2zR0M2UEb8K_o1RSvOlVnGTAVeRisSo3mcz5foEY7WOtazv5itjsG7r6rPxyfbq-IrJU5NjsYq9fl0zAIoTuERKrYnCuuZ1ipGN2ji74NT9pgY0CYZ0HJOSUZfnj5ODNDswyXia9RCquz1KVi2NU6cfrTPW6vBhSKTKpKcdirQKFcXqLM", "token_type": "Bearer", "expires_in": 3600, "scope": "playlist-modify-public user-library-read", "expires_at": 1593399282, "refresh_token": "AQCIi9N-Hno9JJbDcFfJVJLjLbL72_t4Q9zIshzFt-fRl-JLJ8lrJHunM-Ib4QnMaH7uYLWLpr-EWIZU3ylXo14XTD2-evv_YEbJTPfT1IsWa4DmmEjQHL4X4nNxtgXeH70"}
scope = 'user-library-read playlist-modify-public'
import os
import spotipy


def prompt_for_user_token(username, scope=None, client_id = None,
        client_secret = None, redirect_uri = None):
    ''' prompts the user to login if necessary and returns
        the user token suitable for use with the spotipy.Spotify 
        constructor

        Parameters:

         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app

    '''

    if not client_id:
        client_id = os.getenv('SPOTIPY_CLIENT_ID')

    if not client_secret:
        client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    if not redirect_uri:
        redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

    if not client_id:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

            Get your credentials at     
                https://developer.spotify.com/my-applications
        ''')
        raise spotipy.SpotifyException(550, -1, 'no credentials set')

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, 
        scope=scope, cache_path=(".cache-" + username )

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        print('''

            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.

        ''')
        auth_url = sp_oauth.get_authorize_url()
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except:
            print("Please navigate here: %s" % auth_url)

        print()
        print()
        try:
            response = raw_input("Enter the URL you were redirected to: ")
        except NameError:
            response = input("Enter the URL you were redirected to: ")

        print()
        print() 

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None