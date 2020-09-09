# coding=utf-8
from __future__ import unicode_literals
import Tkinter

import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '~/Desktop/songs/%(title)s-%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def show_entry():
    x = e1.get()
    filenames = x
    try:
        youtube_dl.YoutubeDL(ydl_opts).download([filenames])
        label = Tkinter.Label(window, text="Downloaded.", bg='yellow')
        w.create_window(250, 150, window=label)

    except:
        label = Tkinter.Label(window, text="Did not Downloaded, try again", bg='yellow')
        w.create_window(250, 150, window=label)


if __name__ == "__main__":
    window = Tkinter.Tk()
    window.title("Mp3 Downloader")
    # Code to add widgets will go here...

    l = Tkinter.Label(window, text="Past the link above !!")
    l.pack()
    m = Tkinter.Label(window, text="====")
    m.pack()

    w = Tkinter.Canvas(window, width=500, height=400)
    w.pack()
    e1 = Tkinter.Entry(window, width=50)
    w.create_window(250, 50, window=e1)

    butt = Tkinter.Button(text='Download', command=show_entry, highlightbackground='#3E4149', font="Helvetica", pady=2)
    w.create_window(250, 90, window=butt)

    window.mainloop()
