# Spotify Podcast Automation App

Welcome to our Podcast Automation App! We hope this application makes it easier for you to stay up-to-date on all your favorite podcasts using Spotify.

## Application Overview

We built this application becasue Spotify does not always keep their listeners in the loop on their favorite podcasts. Spotify does not currently have a native way to notify users when the podcasts they follow add new episodes, leaving it up to their users to manually check every day ot see if an episode was added.

This application automatically updates a playlist in your Spotify library with the latest episodes from the podcasts you have followed. It then sends you a daily email with a summary of what has been added, so you can easily keep up with your favorite shows in an organized and hands-free way.

## Application Setup

The fastest way to get started is to fork this repository and clone a local copy onto your device. Once you have done that follow these steps:

* Step 1: Create an environment with the latest version of Python and install the requirements file

        conda create -n spotify-podcast-env python=3.7
        pip install -r requirements.txt

* Step 2: Request and save all your needed API keys
    * Spotify API:
        * Visit https://developer.spotify.com/dashboard/ and login using your primary Spotify account
        * Click "CREATE AN APP" and complete the required form
        * Go to app settings and add `https://localhost:8080` as a redirect URI
    * Sendgrid API:
        * Create a free account at https://sendgrid.com/
        * Navigate to https://app.sendgrid.com/settings/api_keys and click "Create API Key"
        * Build a dynamic template and inlcude the following HTML in the body of the email:  

                {{#each episode_info}}
	                {{this.show}}: {{this.name}}
                {{/each}}

* Step 3: Set your environment variables
    * SPOTIFY_CLIENT_ID
    * SPOTIFY_CLIENT_SECRET
    * SPOTIFY_REDIRECT_URI = "http://localhost:8080"
    * SENDGRID_API_KEY
    * SENDGRID_TEMPLATE_ID
    * MY_EMAIL
    * TO_EMAIL

* Step 4: Complete the one-time Podcast Automation App Activation & run the app locally

        FLASK_APP=web_app flask run
    Once your web browser opens, navigate to the provided link and follow the instructions. You can run the app locally after the initial authorization using the following script:
        
        python web_app/email_update.py

* Step 5: Deploy on Heroku
    * Follow Heroku setup guide to get the application deployed on a server
    * Add a Heroku Scheduler addon to the server and set it to run `python -m web_app/email_update.py` once a day
    * Set your config variables
        * heroku config:set SENDGRID_API_KEY
        * heroku config:set SENDGRID_TEMPLATE_ID
        * heroku config:set MY_EMAIL
        * heroku config:set TO_EMAIL

## Quick Overview of the Repo's Files

* web_app.home_routes.py is the primary Flask application that processes the users Spotify credentials, authorizes the application to access the user's account, and then runs the playlist management and email functions locally 

* email_update.py is a primary application that automatically updates your Favorite Podcasts playlist and then calls the Sendgrid API to send you an email with a summary of activity

* playlist_creator.py is a one time function that creates your Favorite Podcasts playlist

* playlist_management.py contains all the functions necessary to continuously update your playlist, including checking which Podcast shows you follow, adding episodes to your playlist, and pulling information about the added episodes

* spotify_auth.py contains the functions to authorize the Podcast Automation App to access your Spotify account and generate a token for the other scripts to use 

