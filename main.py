#main.py --Texted base runner that you can manually add song by song through spotify api

import Check
import Spot

import Deez
deez = Deez.authDeez()
spo = Spot.auth()
title = input("\nWhat should the title of this playlist be: ")
id = spo.me()['id']

playlist = spo.user_playlist_create(id,title)

while True:
    song = input("\nEnter the name of the Song you are Looking for: ")
    artist = input("\nEnter the name of the Artist: ")
    songLink = Spot.find(artist= artist, songname= song)
    if len(songLink) > 4:
        playlistid = Check.checkPlaylist(spo,title)
        if(Check.checkSong(artist, song, songLink,spo)):
            songLink = [songLink]
            spo.playlist_add_items(playlistid,songLink)
        else:
            print("Something went wrong try another song")
    else:
        print("This song does not exist or was not found in my systems, Sorry")


