from pyrogram import Client
from pyrogram.errors import BadRequest
from asyncio import * 
from functions import *
from constants import API_ID, API_HASH, INITIAL_BIO

db = get_db()
app = Client("spotifytgbio", API_ID, API_HASH, no_updates=True)

async def worker(app):
    me = await app.get_me()
    while True:
        current_bio = (await app.get_chat(me.id)).bio
        scp = get_current_playing()
        if scp and "is_playing" in scp:
            if scp["is_playing"] == True:
                artist = scp["item"]["artists"][0]["name"]
                song = scp["item"]["name"]
                bio = f"🎵 {artist} - {song}"
                bio = bio if len(bio) <= 70 else INITIAL_BIO
                if bio != current_bio:
                    await app.update_profile(bio=bio)
                    print(f"[LOG] Updated bio to {bio}")
            else:
                if current_bio != INITIAL_BIO:
                    await app.update_profile(bio=INITIAL_BIO)
                    print(f"[LOG] Updated bio to {INITIAL_BIO}")
        else:
            if current_bio != INITIAL_BIO:
                await app.update_profile(bio=INITIAL_BIO)
                print(f"[LOG] Updated bio to {INITIAL_BIO}")
        await sleep(5)

app.start()
get_event_loop().run_until_complete(worker(app))

idle()
