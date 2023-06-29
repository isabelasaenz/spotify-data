### Spotify Data Analysis
***
This Notebook contains code for analyzing Spotify user data using the Spotify API.

Before running the code, make sure you have the Spotify API credentials (client ID, client secret, and redirect URI)
***
The code performs the following steps:

1. Authenticates Spotify using OAuth2 session and obtains an access token.
2. Retrieves the user's top tracks and top artists from Spotify API.
3. Creates dataframes for the top tracks, top artists, and top albums.
4. Displays the data in tables using matplotlib.
***
#### Results

##### Top Tracks

| Track              | Artist          |
| ------------------ | --------------- |
| Track 1            | Artist 1        |
| Track 2            | Artist 2        |
| ...                | ...             |

##### Top Artists

| Artist             |
| ------------------ |
| Artist 1           |
| Artist 2           |
| ...                |

##### Top Albums

| Album              | Artist          |
| ------------------ | --------------- |
| Album 1            | Artist 1        |
| Album 2            | Artist 2        |
| ...                | ...             |

***
#### Packages used

- **spotipy**: authentication, fetching user data, and managing playlists.

- **pandas**: data structures and functions to handle structured data, such as creating dataframes and performing operations on them.

- **seaborn**: statistical graphics.

- **matplotlib**: plots, charts, and visualizations.

- **requests_oauthlib**: access tokens for OAuth 2.0 protected resources, such as the Spotify API.

- **IPython.display**: displaying images, HTML, and interactive widgets.
***
### Documentation

- [Spotipy Documentation](https://spotipy.readthedocs.io/en/2.22.1/)
- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api)
***
