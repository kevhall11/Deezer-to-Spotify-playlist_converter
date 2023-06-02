#Deez.py   --the deezer wrapper for the purpose of my application

import Secrets
import deezer
from deezer import *

#allows for deezer object to be returned using the Deezer API
def authDeez():
    deez = deezer.Client(app_id=Secrets.deezApp, app_secret=Secrets.deezSecret,)
    return deez

#with the given url and deezer client object it finds the playlist and returns the playlist
#object.
def findPlaylist(url, deez:deezer.Client):
    #deezer playlists have an 11 digit id at the end of the URL which I pick off of and insert
    #into the API
    n = len(url) - 11
    id = url[n:]
    playlist:deezer.Playlist = deez.get_playlist(int(id))
    return playlist

#Using a deezer playlist object it takes every head artist inside and place it into an array
#Which is returned
def getArtistArray(playlist:deezer.Playlist):
    artists = []
    tracks = playlist.get_tracks()
    for track in tracks:
        artistObj = track.get_artist()
        artists.insert(0,artistObj.name)
    return artists

#intakes a deezer playlist object and retuns an array of the song names that are inside
def getSongArray(playlist:deezer.Playlist):
    songs = []
    tracks = playlist.get_tracks()
    for track in tracks:
        songs.insert(0, track.title)
    return songs