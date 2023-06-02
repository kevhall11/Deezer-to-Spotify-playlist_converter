#Check.py   --a class used for different checks varifications or other methods I wanted to use
#with this project
#Kevin Halleran
#6/2/2023

from spotipy import *
import deezer
import Spot
import Deez


#using the spotify api I take in the artist, song name, id and spotify object and returns true
#if the song name and artist match the return of the id api call
def checkSong(artist, song, id, spo:Spotify):
    trac = spo.track(id, market= 'US')
    artist = artist.lower()
    song = song.lower()
    name = findName(trac["artists"])
    if(trac["name"].lower() != song):
        return False
    if artist in name:
        return True
    else:
        return False

#takes in the spotify object and a playlist name and searches for the name of the playlist
#this returns the plaulist id or -1 if the playlist does not exist in the users library
def checkPlaylist(spo:Spotify, playlistName):
    names = spo.current_user_playlists()
    names = names['items']
    for key in names:
        if key['name'].__contains__(playlistName):
            return key['id']
            break
    return -1

#idk why I made this
def createPlaylist(spo:Spotify, name):
    spo.user_playlist_create(spo, name)

#takes in a list from the spotify track and puts every artist from the list into an array which
#is returned and compared to the deezer artists to find a match in songs
def findName(lis:list):
    x:int = len(lis)
    name:list = []
    while (x > 0):
        nam = lis[0]
        name.insert(0,nam["name"].lower())
        x -= 1

    return name

#takes in a deezer playlist object and a spotify object. this compares the songs in the deezer
#playlist with the songs that the spotify api is able to find. every song from the spotify api
#that is found is then returned in an array. these are returned as links so the array can be put
#directly into the spotify api to be added to the main playlist
def songArray(playlist:deezer.Playlist, spo:Spotify):
    songs = []
    artists = Deez.getArtistArray(playlist)
    song = Deez.getSongArray(playlist)
    together = [artists, song]
    if len(artists) != len(song):
        return
    else:
        for x in range(len(together[0])):
            url = Spot.find(together[0][x], together[1][x])
            if(len(url) > 3):
               if checkSong(together[0][x], together[1][x], url, spo):
                   songs.insert(0,url)
        return songs

