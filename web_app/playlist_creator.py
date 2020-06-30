# Playlist generator using authorized credentials and links within app
import spotipy

# Pull written username from web_app, check auth, create playlist
def podcast_playlist_generator(username, token):
    sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        if i or item["name"] != "Podify":
            sp.user_playlist_create(username, "Podify", public=True, description='Latest Episodes') 
        else:
            break