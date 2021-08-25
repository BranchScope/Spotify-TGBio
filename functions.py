import requests, json, os
from constants import API_ID, API_HASH, CLIENT_ID, CLIENT_SECRET, INITIAL_BIO

def get_db():
    if os.path.exists("./database.json"):
        return json.load(open("./database.json"))
    else:    
        create_db()
        return get_db()

def create_db():
    print(f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=https://example.com/callback&scope=user-read-playback-state%20user-read-currently-playing")
    INITIAL_TOKEN = input(f"Click on the link above and paste the param you find on \"code=\": ")
    tokens = get_spotify_tokens(CLIENT_ID, CLIENT_SECRET, INITIAL_TOKEN)
    database = {
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"]
    }
    json.dump(database, open("./database.json", "w"), indent=4)

def get_spotify_tokens(CLIENT_ID, CLIENT_SECRET, INITIAL_TOKEN):
    body = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": "https://example.com/callback",
        "code": INITIAL_TOKEN
    }
    r = requests.post("https://accounts.spotify.com/api/token", data=body)
    return r.json()

def refresh_token():
    database = get_db()
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": database["refresh_token"]
    }
    r = requests.post("https://accounts.spotify.com/api/token", data=data)
    try:
        database["refresh_token"] = r.json()["refresh_token"]
    except KeyError:
        pass
    database["access_token"] = r.json()["access_token"]
    with open("./database.json", "w") as outfile:
        json.dump(database, outfile, indent=4)

def get_current_playing():
    database = get_db()
    oauth = {
        "Authorization": "Bearer " + database["access_token"]
    }
    r = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=oauth)
    if r.status_code == 200 or r.status_code == 204:
        return r.json()
    elif r.status_code == 401:
        refresh_token()
        return get_current_playing()
    elif r.status_code == 429:
        print("[LOG] Too many requests, trying again next time...")
    elif r.status_code == 502:
        print("[LOG] Spotify is down, i'll re-try soon.")