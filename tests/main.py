from pyrogram import Client
from functions import *
from constants import CLIENT_ID, CLIENT_SECRET, INITIAL_BIO

db = get_db()

if db == None:
    db = create_db()
    
print(get_current_playing())