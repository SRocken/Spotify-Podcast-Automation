# Playlist generator using authorized credentials and links within app
import spotipy

# Pull written username from web_app, check auth, create playlist
def podcast_playlist_generator(username, token):
    sp = spotipy.Spotify(auth=token) #calls spotipy with authorized credentials
    results = sp.current_user_playlists(limit=50)
    playlists_items = results['items']
    playlists_names = []
    for x in playlists_items:
        playlists_names.append(x['name'])

    #Check if "Podify" Playlist exists, if not, create. If it does, print "Podify Playlist Exits"
    if 'Podify' not in playlists_names:
        playlist = sp.user_playlist_create(username, "Podify", public=True, description='Latest Episodes') #Consider branding app & playlist name
        print("Podify playlist created")
    else:
        print("Podify playlist already exists")

