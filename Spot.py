#K.Halleran
#Spot.py  --wrapper spotipy API that I am using to work with my playlist converter
#5/31/2023


import spotipy
from spotipy import *
import Secrets
from googlesearch import search
import time
#this is for authentiation with a redirect uri so users can log on and verify their spotify accounts
#it returns the spotify object that contains all nessecry tokens
def auth():
    scope = "playlist-modify-public"
    auth_manager = SpotifyOAuth(client_id= Secrets.clientId, client_secret= Secrets.clientSecret, redirect_uri= "http://localhost:8080",scope= scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

#contains wrapper method becuase i forgot about __contains__() until I did this
def contains(start, str):
    if (start.__contains__(str)):
        return True
    else:
        return False

#takes in an array of songs along with the spotify object and playlist id
#all songs in the array are added to the specified playlist uring the spotify object
def addSongArray(song , spo:Spotify, playlistid):
    for songs in song:
        songs = [str(songs)]
        spo.playlist_add_items(playlist_id= playlistid, items= songs)

#Uses the google API to search for a specific link that I am looking for, After finding the link
#it will check certian data fields and return the link
def find(artist, songname):
    ser = "spotify.com/track/ " + artist + " " + songname
    final = ""
    time.sleep(2)
    for url in search(ser, stop=3):
        if(contains(url,"spotify.com/track")):
            final = url
            break
        if(contains(url,"spotify.link")):
            for ser in search(url, stop = 1):
                if(contains(ser, "spotify.com/track")):
                    final = ser
                    break
    if(len(final) > 1):
        return(final)
    else:
        return -1

