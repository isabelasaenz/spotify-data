!pip install spotipy ipyauth requests_oauthlib

import spotipy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
import json
import IPython.display

from spotipy.oauth2 import SpotifyOAuth
from requests_oauthlib import OAuth2Session

# API credentials and settings
client_id = '<client id>'
client_secret = '<client secret>'
redirect_uri = '<redirect uri>'
scope = 'user-top-read'

# function to authenticate spotify and get access token
def authenticate_connection(client_id, client_secret, redirect_uri, scope):
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    authorization_url, state = oauth.authorization_url("https://accounts.spotify.com/authorize")

    print(f"go to the following URL and authorize access: {authorization_url}")
    authorization_response = input("enter the callback URL: ")

    token = oauth.fetch_token(
        "https://accounts.spotify.com/api/token",
        authorization_response=authorization_response,
        client_secret=client_secret,
    )
    access_token = token["access_token"]
    return access_token

# authenticate spotify and get access token
access_token = authenticate_connection(client_id, client_secret, redirect_uri, scope)
# create client object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id ,
                                                client_secret,
                                                redirect_uri,
                                                scope="user-top-read user-library-read"))

time_range = 'short_term' # 'short_term = 4 weeks', 'medium_term = 6 months', 'long_term = all time'
top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=10, offset=0)
top_artists = sp.current_user_top_artists(time_range=time_range, limit=5, offset=0)

# create a list of tuples containing album and artist names
album_artist_pairs = []
for track in top_tracks['items']:
    album = track['album']['name']
    artist = track['artists'][0]['name']
    album_artist_pairs.append((album, artist))

# remove duplicates from the list
unique_album_artist_pairs = list(set(album_artist_pairs))

# create the dataframes

tracks_df = pd.DataFrame([(track['name'], track['artists'][0]['name']) for track in top_tracks['items']],
                         columns=['Track', 'Artist'])
print("Top Tracks:")
print(tracks_df)

artists_df = pd.DataFrame([{'Artist': artist['name']} for artist in top_artists['items']])
print("\nTop Artists:")
print(artists_df)

albums_df = pd.DataFrame(unique_album_artist_pairs, columns=['Album', 'Artist'])
print("\nTop Albums:")
print(albums_df)

def create_table(df, title):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')

    # create table with custom colors
    cell_colors = [["#efefef"] * len(df.columns) if i % 2 == 0 else ["#ffffff"] * len(df.columns) for i in range(len(df))]
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', cellColours=cell_colors)

    # set font size and scale
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)

    # adjust cell padding
    table.auto_set_column_width(list(range(len(df.columns))))

    # remove table borders
    for key, cell in table.get_celld().items():
        cell.set_linewidth(0)

    # adjust spacing around "top artists" table
    if title == 'Top Artists':
        table.scale(1.5, 1)

    # set title
    ax.text(0.5, 0.95, title, fontsize=16, ha='center', va='bottom', transform=ax.transAxes)

    plt.show()

create_table(tracks_df, 'Top Tracks')

create_table(artists_df, 'Top Artists')

create_table(albums_df, 'Top Albums')