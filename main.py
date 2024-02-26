from tkinter import *

from dotenv import load_dotenv
load_dotenv()

from splash_screen import splash_screen
from entryScreen import player_entry_screen

import os
from supabase import create_client, Client


#initialize supabase
url = os.environ.get("https://rjexhdkzwhcnrcuvzute.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJqZXhoZGt6d2hjbnJjdXZ6dXRlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDc3NjAwMTMsImV4cCI6MjAyMzMzNjAxM30.2MMcSmeZo85VlCMBsPI0ehCnGBrCiIZoqx722bQA0C4")
supabase = create_client(url,key)

splash_screen()
player_entry_screen(supabase)


# Starts up the udp server
# def startUDP():
#     command = ["python3", "UDP_Client.py"]
#     subprocess.run(command)

