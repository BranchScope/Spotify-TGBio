from pyrogram import Client
from asyncio import * 
from functions import *

db = get_db()
if db == None:
    db = create_db()

app = Client("spotifytgbio", API_ID, API_HASH)
    
async def worker(app):
    while True:
        scp = get_current_playing()
        if scp["is_playing"] == True:
            artist = scp["item"]["artists"][0]["name"]
            song = scp["item"]["name"]
            bio = f"🎵 {artist} - {song}"
            if bio != (await app.get_chat((await app.get_me()).id)).bio:
                await app.update_profile(bio=bio)
                print(f"Updated bio to {bio}")
        await sleep(5)

app.start()
get_event_loop().run_until_complete(worker(app))

idle()