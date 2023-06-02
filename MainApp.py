#MainApp.py     -really basic gui using tkinter 
#Kevin Halleran 6-2-2023

from tkinter import *
import PlaylistConverter
from tkinter import messagebox

window = Tk()
title = "Deezer to Spotify Website Converter"
window.title(title)

window.geometry('400x350')

playlist = Label(window, text= 'What would you like your Playlist name to be?')
playlist.grid(column = 0, row = 4)
playlistName = Entry(window, width= 50)
playlistName.grid(column=1, row=4)
link = Label(window, text= 'What is the Link of your Deezer playlist?')
link.grid(column= 0, row = 5)
deezerLink = Entry(window, width= 50)
deezerLink.grid(column= 1, row= 5)




def submitButton():
    playEntry = playlistName.get()
    link = deezerLink.get()
    deezerLink.configure(state= 'disabled')
    playlistName.configure(state= 'disabled')
    num = PlaylistConverter.main(playEntry, link)
    if(num>0):
        messagebox.showinfo(title, 'Your Playlist Has been Succesfully Created')
    else:
        messagebox.showinfo(title, 'Sorry, there has been a problem creating your playlist')
    deezerLink.configure(state= 'normal')
    playlistName.configure(state= 'normal')

button = Button(window, text= "Submit", command= submitButton)
button.grid(column= 0, row= 6)

window.mainloop()
