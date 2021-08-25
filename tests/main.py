import requests, json, os
from pyrogram import Client
from constants import CLIENT_ID, CLIENT_SECRET, INITIAL_BIO

#if os.path.isfile('./database.json'):
#    os.remove('database.json')

def get_db():
    return json.load(open("./database.json"))

def get_spotify_tokens(CLIENT_ID, CLIENT_SECRET, INITIAL_TOKEN, INITIAL_BIO):
    body = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": "https://example.com/callback",
        "code": INITIAL_TOKEN
    }
    r = requests.post("https://accounts.spotify.com/api/token", data=body)
    info = r.json()
    database = {
        'access_token': info['access_token'],
        'refresh_token': info['refresh_token'],
        'bio': INITIAL_BIO,
    }
    with open('./database.json', 'w') as outfile:
        json.dump(database, outfile, indent=4)

def refresh_token():
    database = get_db()
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": database['refresh_token']
    }
    r = requests.post("https://accounts.spotify.com/api/token", data=data)
    try:
        database['refresh_token'] = r.json()['refresh_token']
    except KeyError:
        pass
    database['access_token'] = r.json()['access_token']
    with open('./database.json', 'w') as outfile:
        json.dump(database, outfile, indent=4)


def get_current_playing():
    database = get_db()
    oauth = {
        "Authorization": "Bearer " + database['access_token']
    }
    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=oauth)
    if r.status_code == 200 or r.status_code == 204:
        return r.text
    elif r.status_code == 401:
        r_token = refresh_token()

#INITIAL_TOKEN = input(f"Click at this link and paste the porcodio you find on \"code=\" [https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-playback-state%20user-read-currently-playing]: ")

#get_spotify_tokens(CLIENT_ID, CLIENT_SECRET, INITIAL_TOKEN, INITIAL_BIO)
print(get_current_playing())
