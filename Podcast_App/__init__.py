# app/__init__.py

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
