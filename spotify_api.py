import os

import requests

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type'   : 'client_credentials',
    'client_id'    : CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
print("got access token")

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'


# Track ID from the URI
# album_id = '4YZI5RGjvxQsZmeY8ewpxs'

# actual GET request with proper header
# r = requests.get(BASE_URL + 'albums/' + album_id, headers=headers)
# r = r.json()


def get_album_name(album_id: str) -> str:
    r = requests.get(BASE_URL + 'albums/' + album_id, headers=headers)
    
    r = r.json()
    return r['name']


def get_name_from_link(link: str) -> str:
    link = link.split("/")
    item_id = link[-1]
    item_type = link[-2]
    
    get_link = BASE_URL + f"{item_type}s/" + item_id
    
    r = requests.get(get_link, headers=headers)
    
    r = r.json()
    return r['name']


def get_playlist_name(playlist_id: str) -> str:
    r = requests.get(BASE_URL + 'playlists/' + playlist_id, headers=headers)
    
    r = r.json()
    return r['name']


def get_track_name(track_id: str) -> str:
    r = requests.get(BASE_URL + 'tracks/' + track_id, headers=headers)
    
    r = r.json()
    return r['name']
