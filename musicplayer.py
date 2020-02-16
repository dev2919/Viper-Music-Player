import tkinter.messagebox
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pause
import time
import threading
import pygame
from tkinter import ttk
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

root = Tk()

style = ttk.Style()

root.configure(background='white')

menubar = Menu(root)

root.config(menu=menubar)

playlist = []

subMenu = Menu(menubar, tearoff=0)

root.style = ttk.Style()


paused = False


mixer.init()

root.geometry('900x250')

root.title("Music")

index = 0

root.iconbitmap(r"Music.ico")

labelfont = ('nexa bold', 20, 'bold')
filelabel = Label(root, text='Playing')
filelabel.pack(pady=10)
filelabel.config(bg='white', fg='Black', anchor="n", justify='right')
filelabel.config(font=labelfont)
filelabel.config(height=3, width=20)
filelabel.place(x=250, y=35)

labelfont = ('nexa bold', 10, 'bold')
lengthlabel = Label(root, text='--:--')
lengthlabel.pack()
lengthlabel.place(x=370, y=100)
lengthlabel.config(bg='white', fg='Black')
lengthlabel.config(font=labelfont)
lengthlabel.config(height=3, width=20)

labelfont = ('nexa bold', 10, 'bold')
llabel = Label(root, text='Volume')
llabel.pack()
llabel.place(x=370, y=100)
llabel.config(bg='white', fg='Black')
llabel.config(font=labelfont)
llabel.place(x=580, y=150)

labelfont = ('nexa bold', 10, 'bold')
currenttimelabel = Label(root, text='--:--')
currenttimelabel.pack()
currenttimelabel.place(x=250, y=100)
currenttimelabel.config(bg='white', fg='Black')
currenttimelabel.config(font=labelfont)
currenttimelabel.config(height=3, width=20)

artlabel = Label(root, text='Artist')
labelfont = ('nexa bold', 10, 'bold')
artlabel.pack()
artlabel.config(bg='white', fg='Black', anchor="n", justify='center')
artlabel.config(font=labelfont)
artlabel.place(x=375, y=80)

postphoto = PhotoImage(file='Art/def.png')
labelphoto = Label(root, image=postphoto)
labelphoto.pack()
labelphoto.place(x=20, y=10)

playlistbox = Listbox(root)
playlistbox.pack()
playlistbox.place(x=700, y=20)


def browse_file():
    global filename_path
    global b
    filename_path = filedialog.askopenfilename()
    f = filename_path
    b = os.path.splitext(os.path.basename(f))[0]
    a = ' '+ b
    if a ==' ':
        messagebox.showerror("Error", "File Not Found, Please Open!")
        browse_file()
    else:
        add_to_playlist(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)



def about_us():
    tkinter.messagebox.showinfo('About Music Player', 'This is a music player build using Python Tkinter by us')


def poster_call():
    try:
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        play_it = playlist[selected_song]
        artist_name = os.path.splitext(os.path.basename(play_it))[0]
        url = 'C:/Users/dev29/PycharmProjects/Music/Art/' + artist_name + '.png'
        uphoto = PhotoImage(file=url)
        labelphoto.configure(image=uphoto)
        labelphoto.image = uphoto
    except:
        url = 'C:/Users/dev29/PycharmProjects/Music/Art/def.png'
        uphoto = PhotoImage(file=url)
        labelphoto.configure(image=uphoto)
        labelphoto.image = uphoto



def show_details(play_song):
    file_data = os.path.splitext(play_song)
    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

        # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = ' ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
    # Continue - Ignores all of the statements below it. We check if music is paused or not.
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if pause.paused== False:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = ' ' + timeformat
            time.sleep(1)
            current_time += 1
        elif pause.paused == True:
            continue



def play_btn():
    poster_call()
    if pause.paused == False:
        try:
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            filelabel['text'] = ' ' + os.path.splitext(os.path.basename(play_it))[0]
            mixer.music.play()
            show_details(play_it)
            try:
                track = MP3(play_it)
                tags = ID3(play_it)
                artist = tags['TPE1'].text[0]
                artlabel['text'] = artist
            except:
                artlabel['text'] = 'unknown'

        except:
            messagebox.showerror("Error", "File Not Found, Please Open!")

    elif pause.paused == True:
        mixer.music.unpause()
        pause.paused = FALSE
        playBtn.configure(image=playPhoto)



def stop_btn():
    pause_music.paused = False
    mixer.music.stop()


def loop_btn():
    time.sleep(1)
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    play_it = playlist[selected_song]
    pygame.mixer.music.load(play_it)
    pygame.mixer.music.play(-1)
    show_details(play_it)


def pause_music():
    pause.paused = True
    mixer.music.pause()


def set_volume(vol):
    mixer.music.set_volume(float(vol) / 100)


def next_btn():
    stop_btn()
    file = playlistbox.curselection()
    next_selection = 0
    if len(file) > 0:
        last_selection = int(file[-1])

        playlistbox.selection_clear(file)
        if last_selection < playlistbox.size() - 1:
            next_selection = last_selection + 1

    track = MP3(filename_path)
    tags = ID3(filename_path)
    artist=tags['TPE1'].text[0]
    artlabel['text']=artist
    playlistbox.activate(next_selection)
    playlistbox.selection_set(next_selection)
    play_btn()


def prev_btn():
    stop_btn()
    file = playlistbox.curselection()
    next_selection = 0
    if len(file) > 0:
        last_selection = int(file[-1])
        playlistbox.selection_clear(file)
        if last_selection < playlistbox.size():
            next_selection = last_selection - 1
    elif len(file) ==0:
        messagebox.showerror("Error","End of list or empty")

    playlistbox.activate(next_selection)
    playlistbox.selection_set(next_selection)
    play_btn()

muted = FALSE

def mute_music():
    global muted
    if muted:  # Unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        volume.set(50)
        muted = FALSE
    else:  # mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        volume.set(0)
        muted = TRUE

def on_closing():
    stop_btn()
    root.destroy()

menubar.add_cascade(label=".  .  .", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_btn, borderwidth=0, highlightthickness=0)
stopBtn.pack()
stopBtn.place(x=460, y=150)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pause_music, borderwidth=0, highlightthickness=0)
pauseBtn.pack()
pauseBtn.place(x=410, y=150)

playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=play_btn, borderwidth=0, highlightthickness=0)
playBtn.pack()
playBtn.place(x=310, y=150)

mutePhoto = PhotoImage(file='mute.png')
volumePhoto = PhotoImage(file='volume.png')
volumeBtn = Button(root, image=volumePhoto, command=mute_music,borderwidth=0, highlightthickness=0)
volumeBtn.pack()
volumeBtn.place(x=510,y=150)

volume = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=set_volume)
style.configure('TScale', background='white')
volume.pack()
volume.set(70)
set_volume(70)
volume.place(x=580, y=170)

addbtn = Button(root, text='  +  ', command=browse_file, background='white', borderwidth=0, highlightthickness=0)
addbtn.pack()
addbtn.place(x=699, y=185)

delbtn = Button(root, text='  -  ',command=del_song, background='white', borderwidth=0, highlightthickness=0)
delbtn.pack()
delbtn.place(x=730, y=185)

loopPhoto = PhotoImage(file='repeat.png')
loopbtn = Button(root, image=loopPhoto,command=loop_btn, background='white', borderwidth=0, highlightthickness=0)
loopbtn.pack()
loopbtn.place(x=260,y=100)

prevPhoto = PhotoImage(file='previous.png')
prevBtn = Button(root, image=prevPhoto, command=prev_btn, borderwidth=0, highlightthickness=0)
prevBtn.place(x=260, y=150)

nextPhoto = PhotoImage(file='next.png')
nextBtn = Button(root, image=nextPhoto, command=next_btn, borderwidth=0, highlightthickness=0)
nextBtn.place(x=360, y=150)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()