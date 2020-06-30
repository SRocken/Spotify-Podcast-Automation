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


## Deploy To Heroku Server Setup
* Deploy on Heroku Directions Repurposed From: Prof Rossetti @ https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/web-service/deploying.md
  

    * Step 1: If you haven't yet done so, [install the Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up), and make sure you can login and list your applications.
    * Step 2:Use the online [Heroku Dashboard](https://dashboard.heroku.com/) or the command-line (instructions below) to [create a new application server](https://dashboard.heroku.com/new-app), specifying a unique name (e.g. "notification-app-123", but yours will need to be different): 
        heroku create notification-app-123 # choose your own unique name!
    * Step 3: Verify the app has been created:
        heroku apps
    * Step 4: Also verify this step has associated the local repo with a remote address called "heroku":
        git remote -v
    * Step 5: Before we copy the source code to the remote server, we need to configure the server's environment in a similar way we configured our local environment.

    Instead of using a ".env" file, we will directly configure the server's environment variables by either clicking "Reveal Config Vars" from the "Settings" tab in your application's Heroku dashboard, or from the command line (instructions below):

    ![a screenshot of setting env vars via the app's online dashboard](https://user-images.githubusercontent.com/1328807/54229588-f249e880-44da-11e9-920a-b11d4c210a99.png)
    
    or, alternatively...
        # set environment variables:
        heroku config:set APP_ENV="production" 
    heroku config:set MY_EMAIL="___________"
    heroku config:set SENDGRID_API_KEY="___________"
    heroku config:set SENDGRID_TEMPLATE_ID="___________" 
    heroku config:set SPOTIPY_CLIENT_IDE="___________"      
    heroku config:set SPOTIPY_CLIENT_SECRET="___________"   
    heroku config:set SPOTIPY_REDIRECT_URI="___________"   
    heroku config:set TO_EMAIL="___________"   
    heroku config:set username="___________"   
    * Step 6: After this configuration process is complete, you are finally ready to "deploy" the application's source code to the Heroku server:
        git push heroku master
    * Step 7: Once you've deployed the source code to the Heroku server, login to the server to see the files there, and take an opportunity to test your ability to run the script that now lives on the server:
        heroku run bash # login to the server
        # ... whoami # see that you are not on your local computer anymore
        # ... ls -al # optionally see the files, nice!
        # ... python -m app.daily_briefing # see the output, nice!
        # ... exit # logout
    * Step 8: Finally, provision and configure the server's "Heroku Scheduler" resource to run the notification script at specified intervals, for example once per day.

    From the "Resources" tab in your application's Heroku dashboard, search for an add-on called "Heroku Scheduler" and provision the server with a free plan.

    ![a screenshot of searching for the resource](https://user-images.githubusercontent.com/1328807/54228813-59ff3400-44d9-11e9-803e-21fbd8f6c52f.png)

    ![a screenshot of provisioning the resource](https://user-images.githubusercontent.com/1328807/54228820-5e2b5180-44d9-11e9-9901-13c538a73ac4.png)       

    NOTE: if doing this for the first time, Heroku may ask you to provide billing info. Feel free to provide it, as the services we are using to complete this exercise are all free, and your card should not be charged!

    Finally, click on the provisioned "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the designated python command (`python -web_app/heroku.py`) at a scheduled interval (e.g. every 10 minutes), and finally click to "Save" the job:


## Quick Overview of the Repo's Files

* web_app.home_routes.py is the primary Flask application that processes the users Spotify credentials, authorizes the application to access the user's account, and then runs the playlist management and email functions locally 

* email_update.py is a primary application that automatically updates your Favorite Podcasts playlist and then calls the Sendgrid API to send you an email with a summary of activity. Can be run locally after you have authourized the app using the Flask application

* playlist_creator.py is a one time function that creates your Favorite Podcasts playlist

* playlist_management.py contains all the functions necessary to continuously update your playlist, including checking which Podcast shows you follow, adding episodes to your playlist, and pulling information about the added episodes

* spotify_auth.py contains the functions to authorize the Podcast Automation App to access your Spotify account and generate a token for the other scripts to use 
  
* heroku.py contains the code to automate playlist and email creation on a daily basis. NOTE: This code can only be used once the Web App authorization process has been run first

