import pygame
from  tkinter import *
from tkinter import filedialog

pygame.init()
win = Tk()
win.title("Music Player")
win.geometry("900x300")
win.config(bg='black')

current_index=0
audio_file=['C:\\Users\\bhand\\Downloads\\Heeriye-Heeriye-Aa(PaglaSongs).mp3',
            'C:\\Users\\bhand\\Downloads\\Tere-Bin(PaglaSongs).mp3',
            'C:\\Users\\bhand\\Downloads\\Gasolina(PaglaSongs).mp3',
            'C:\\Users\\bhand\\Downloads\\Udd Jaa Kaale Kaava - Gadar 2 128 Kbps.mp3'
                
            ]

def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Control functions
def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_index
    current_index= (current_index + 1)% len(audio_file)
    pygame.mixer.music.load(audio_file[current_index])
    pygame.mixer.music.play()

def prev_music():
    global current_index
    current_index= (current_index - 1)% len(audio_file)
    pygame.mixer.music.load(audio_file[current_index])
    pygame.mixer.music.play()

f1 = ("arial",20,"bold")

load_bt=Button(win,text="Load Music",font=f1,command=load_music,bg='lightcyan',fg='darkorchid')
load_bt.place(x=360,y=50)

play_bt=Button(win,text="Play",font=f1,command=play_music,bg='lightblue',fg='Red')
play_bt.place(x=250,y=200)

pause_bt=Button(win,text="Pause",font=f1,command=pause_music,bg='lightblue',fg='Red')
pause_bt.place(x=400,y=200)

stop_bt=Button(win,text="Stop",font=f1,command=stop_music,bg='lightblue',fg='Red')
stop_bt.place(x=560,y=200)

next_bt=Button(win,text="Next",font=f1,command=next_music,bg='lightblue',fg='Red')
next_bt.place(x=700,y=200)

previous_bt=Button(win,text="Prev",font=f1,command=prev_music,bg='lightblue',fg='Red')
previous_bt.place(x=100,y=200)

win.mainloop()