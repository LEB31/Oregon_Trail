# Lily Bain  Nightmare Before Christmas Trail Version 1.0
from tkinter import * 
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import ttk 
import random 

# Level Functions

def one():
    start = Toplevel()
    start.title('Intro & Directions')
    start.geometry('600x400')
    start.configure(bg="#A4A4A4")
    load = Image.open('I.png')
    resize = load.resize((275, 175), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(resize) 
    img1 = Label(start, image=render)
    img1.image=render
    img1.place(x=0,y=0)    
    e = Label(start, text= "You're playing as Jack Skellington\n\nYou're only goal is to bring some friends to Christmas Land", bg="#A4A4A4").place(x=280,y=50)
    f = Label(start, text= "Zero, Sally, The Mayor, and The Mummy Boy\n are joining you!", fg="#62247C", bg="#A4A4A4").place(x=320,y=100)
    w = Label(start, text= "Remember, you have to bring at least one person to\n Christmas Land!", fg="#7C2424", bg="#A4A4A4").place(x=300,y=120)
    s = Button(start, text= "Start the Journey",fg= "#6F1F51", bg="#A4A4A4", width= 20,command=trail).place(x=250,y=250)
  
def trail():
    go = Toplevel()
    go.title('On the Path')
    go.geometry('600x400')
    go.configure(bg="#5d3d1f")
    load = Image.open('trail.png')
    resize = load.resize((375, 275), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(resize) 
    img1 = Label(go, image=render)
    img1.image=render
    img1.place(x=0,y=0)  
    # List of distractions
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # Names of group members
    N = ['Zero', 'Sally', 'The Major', 'The Mummy Boy']



# Create a window
win = Tk()
win.title('Trail to Christmas Land')
win.geometry('600x400')
load = Image.open('nbcss.png')
resize = load.resize((600, 400), Image.Resampling.LANCZOS)
render = ImageTk.PhotoImage(resize)
img = Label(win, image=render).place(x=0,y=0)
welcome = Label(win, text="Trail to\nChristmas Land", font="Courier", bg='#fcd462').place(x=230,y=80)
play = Button(win, text="Play", font="Courier", bg='#fcd462', command= one)
play.place(x=280,y=145)

# Variable Nightmare Zone 

win.mainloop()