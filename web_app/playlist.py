# Playlist generator using authorized credentials and links within app
import spotipy

from web_app.spotify_auth import authenication_token, read_username_from_csv


# Pull written username from web_app, check auth, create playlist
def podcast_playlist_generator(username, token):
    sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials 
    sp.user_playlist_create(username, "Favorite Podcasts", public=True, description='Latest Episodes') #Consider branding app & playlist name
