# web_app/__init__.py

import os

import os
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import datetime
load_dotenv()
from utils import prompt_for_user_token


from .client import *  # noqa
from .oauth2 import *  # noqa
from .utils import *  # noqa
from .exceptions import *  # noqa

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
username = os.getenv("username")


from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes

def create_app():
    load_dotenv()

    app_env = os.environ.get("FLASK_ENV", "development") # set to "production" in the production environment
    secret_key = os.environ.get("SECRET_KEY", "super secret") # overwrite this in the production environment
    testing = False # True if app_env == "test" else False
    
    app = Flask(__name__)
    app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, TESTING=testing)
    app.register_blueprint(home_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)