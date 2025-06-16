# from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy

date_selected = input("Which year would u like to travel to?\nEnter a date in this format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date_selected}/"

ClientID = "1ada41f77ccc4a7a8cece2895bf5f4ad"
ClientSecret = "63c398e0b10647b598231fa3b356cbca"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URL = "http://example.com"

# Set up authentication
spotify_auth = spotipy.oauth2.SpotifyOAuth(scope="playlist-modify-private",
                                           client_id=ClientID,
                                           client_secret=ClientSecret,
                                           redirect_uri=REDIRECT_URL,
                                           username="SALMA",
                                           show_dialog=True,
                                           cache_path="token.txt")
# Initialize Spotify client
spotify = spotipy.Spotify(auth_manager=spotify_auth)

# Get user info
user_info = spotify.current_user()
user_id = user_info["id"]
user_name = user_info.get("display_name")

response = requests.get(BILLBOARD_URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
songs = soup.select("ul li ul li h3")
song_names = [song.getText().strip() for song in songs]

song_uris = []
for song_name in song_names:
    data = spotify.search(
        q=f"track: {song_name} year: {date_selected.split("-", 1)}",
        type="track",
    )
    try:
        song_uris.append(data["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = spotify.user_playlist_create(user=user_id, name=f"{date_selected} Billboard 100", public=False)

spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Songs added successfully to the playlist!")
