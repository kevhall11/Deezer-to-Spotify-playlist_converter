#Kevin Halleran
#PlaylistConverter.py   --runner class to convert deezer playlist to spotify

import Check
import Deez
import Spot


def main(title, deezerLink):
    try:
        deez = Deez.authDeez()
        spo = Spot.auth()
        title = title.strip()
        deezerLink = deezerLink.strip()
        id = spo.me()['id']

        playlist = spo.user_playlist_create(id,title)
        playlistid = Check.checkPlaylist(spo, title)
        deezerPlaylist = Deez.findPlaylist(deezerLink, deez)
        songs = Check.songArray(deezerPlaylist, spo)
        spo.playlist_add_items(str(playlistid), songs)
        return 1
    except Exception:
        return -1


