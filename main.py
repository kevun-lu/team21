from tkinter import *

from dotenv import load_dotenv
load_dotenv()
import time
import os
from supabase import create_client, Client
from splash_screen import splash_screen

from entryScreen import player_entry_screen

url = os.environ.get("supabase_url")
key = os.environ.get("supabase_key")
supabase = create_client(url,key)



data, count = supabase.table('players').select('*').eq('id', 2).execute()

print(data[1] == [])
print(count)

#splash_screen()
player_entry_screen(supabase)


