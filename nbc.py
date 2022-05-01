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
    global hour
    go = Toplevel()
    go.title('On the Path')
    go.geometry('600x400')
    go.configure(bg="#e6b8a0")
    load = Image.open('trail.png')
    resize = load.resize((375, 275), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(resize) 
    img1 = Label(go, image=render)
    img1.image=render
    img1.place(x=0,y=0)  

    # Hour Count
    H = Label(go, text="Hour: 1", bg="#e6b8a0", fg="#843c3c")
    H.place(x=475, y=75)

    # List of distractions (lose a group member)
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # List of misfourtunes (lose an hour)
    M = ["Zero lost his bone", "Sally's stitches ripped", "The Mayor lost his hat", "The Mummy Boy unraveled"]
    # Names of group members
    N = ['Zero', 'Sally', 'The Mayor', 'The Mummy Boy']
    # Random
    RM = random.randint(1,50)
    if RM == 16:
        pause1 = Label(go, text= M.index(0), fg ="#843c3c", bg="#e6b8a0").place(x=280, y=150)
    elif RM == 12:
        pause2 = Label(go, text= M.index(1), fg ="#843c3c", bg="#e6b8a0").place(x=280, y=150)
    elif RM == 3:
        pause3 = Label(go, text= M.index(2), fg ="#843c3c", bg="#e6b8a0").place(x=280, y=150)
    elif RM == 23:
        pause4 = Label(go, text= M.index(3), fg ="#843c3c", bg="#e6b8a0").place(x=280, y=150)
    


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

# Hourly Count 
hour = 0 


win.mainloop()