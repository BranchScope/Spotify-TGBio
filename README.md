# Spotify-TGBio
Automatically change your Telegram bio to show what you are listening to on Spotify.

### Requirements
- Python 3.6 or higher.
- A [Telegram API key](https://docs.pyrogram.org/intro/setup#api-keys).
- A [Spotify Application](https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app).

### Installation
``` bash
git clone https://github.com/BranchScope/Spotify-TGBio
cd Spotify-TGBio
pip3 install -r requirements.txt
```

### Configuration
- Put your Telegram `api_id` and `api_hash` in `constants.py`, you can find them by registering a Telegram Application [here](https://my.telegram.org/apps).
- Put your Spotify App's `client_id` and `client_secret` in `constants.py`, you can find them by registering a Spotify Application [here](https://developer.spotify.com/dashboard/applications).
- Put your current Telegram bio in `constants.py`, to restore it when you stop listening to music or when Spotify goes down.

### Start
``` bash
python3 main.py
```

---

### Support/Contributing
Want to contribute? Pull requests are accepted! Do you need help? Feel free to open an issue or to contact me on [Telegram](https://t.me/SpotifyTGBio).

### License
Licensed under the terms of the [MIT License](LICENSE)

---

Join [@SpotifyTGBio](https://t.me/SpotifyTGBio) to stay updated about the project.