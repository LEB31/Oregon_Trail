# Lily Bain  Nightmare Before Christmas Trail Version 1.0
from ast import Delete
from tkinter import * 
from tkinter import PhotoImage
from turtle import update
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
    f = Label(start, text= "Zero, Sally, The Mayor, and The Mummy Boy\n are joining you!", fg="#62247C", bg="#A4A4A4").place(x=320,y=110)
    w = Label(start, text= "Remember, you have to bring at least one person to\n Christmas Land!", fg="#7C2424", bg="#A4A4A4").place(x=300,y=150)
    s = Button(start, text= "Start the Journey",fg= "#6F1F51", bg="#A4A4A4", width= 20,command=trail).place(x=250,y=250)
  
def trail():
    global hour
    global distance
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
    hour = 1
    H = Label(go, text="Hour: " + str(hour), bg="#e6b8a0", fg="#843c3c")
    H.place(x=475, y=45)

    # Distance 
    distance = 50
    if distance >= 40:
        l = Label(go, text="Location: Town", bg="#e6b8a0", fg="#843c3c").place(x=450,y=65)

    # List of distractions (lose a group member)
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # List of misfourtunes (lose an hour)
    M = ["Zero lost his bone", "Sally's stitches ripped", "The Mayor lost his hat", "The Mummy Boy unraveled"]
    # Names of group members
    N = ['Zero', 'Sally', 'The Mayor', 'The Mummy Boy']
    # Random
    RM = random.randint(1,50)
    print(RM)
    if RM == 16:
        pause1 = Label(go, text= "Zero lost his bone", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 12:
        pause2 = Label(go, text= "Sally's stitches ripped", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 3:
        pause3 = Label(go, text= "The Mayor lost his hat", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour += 1
    elif RM == 23:
        pause4 = Label(go, text= "The Mummy Boy unraveled", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    else: 
        hour = hour

    # Energy (Uses Progress Bars)
    Progress = ttk.Progressbar(go, orient = HORIZONTAL, length = 100, mode = 'determinate', value=5).place(x=450,y=100)

    # Next 
    next = Button(go, text="Next", command=trail2).place(x=475,y=200)

    # Supplies 
    check = Button(go, text="Check Supplies", command=checksupplies).place(x=450, y=300)

def trail2():
    global hour
    global distance
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
    hour = 2
    H = Label(go, text="Hour: " + str(hour), bg="#e6b8a0", fg="#843c3c")
    H.place(x=475, y=45)

    # Distance 
    distance = 43
    if distance >= 43:
        l = Label(go, text="Location: Town Gates", bg="#e6b8a0", fg="#843c3c").place(x=440,y=65)

    # List of distractions (lose a group member)
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # List of misfourtunes (lose an hour)
    M = ["Zero lost his bone", "Sally's stitches ripped", "The Mayor lost his hat", "The Mummy Boy unraveled"]
    # Names of group members
    N = ['Zero', 'Sally', 'The Mayor', 'The Mummy Boy']
    # Random
    RM = random.randint(1,50)
    print(RM)
    if RM == 16 or RM == 15 or RM == 44:
        pause1 = Label(go, text= "Zero lost his bone", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
       
    elif RM == 12 or RM == 40 or RM == 5:
        pause2 = Label(go, text= "Sally's stitches ripped", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
        
    elif RM == 3 or RM == 35 or RM == 38:
        pause3 = Label(go, text= "The Mayor lost his hat", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
   
    elif RM == 23 or RM == 37 or RM == 46:
        pause4 = Label(go, text= "The Mummy Boy unraveled", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    

    # Energy (Uses Progress Bars)
    Progress = ttk.Progressbar(go, orient = HORIZONTAL, length = 100, mode = 'determinate', value=10).place(x=450,y=100)

    # Next 
    next = Button(go, text="Next", command=trail3).place(x=475,y=200)

def trail3():
    global hour
    global distance
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
    hour = 3
    H = Label(go, text="Hour: " + str(hour), bg="#e6b8a0", fg="#843c3c")
    H.place(x=475, y=45)

    # Distance 
    distance = 50
    if distance >= 40:
        l = Label(go, text="Location: Graveyard", bg="#e6b8a0", fg="#843c3c").place(x=450,y=65)

    # List of distractions (lose a group member)
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # List of misfourtunes (lose an hour)
    M = ["Zero lost his bone", "Sally's stitches ripped", "The Mayor lost his hat", "The Mummy Boy unraveled"]
    # Names of group members
    N = ['Zero', 'Sally', 'The Mayor', 'The Mummy Boy']
    # Random
    RM = random.randint(1,50)
    print(RM)
    if RM == 16:
        pause1 = Label(go, text= "Zero lost his bone", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 12:
        pause2 = Label(go, text= "Sally's stitches ripped", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour += 1
    elif RM == 3:
        pause3 = Label(go, text= "The Mayor lost his hat", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 23:
        pause4 = Label(go, text= "The Mummy Boy unraveled", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1


    # Energy (Uses Progress Bars)
    Progress = ttk.Progressbar(go, orient = HORIZONTAL, length = 100, mode = 'determinate', value=15).place(x=450,y=100)

    # Next 
    next = Button(go, text="Next", command=trail4).place(x=475,y=200)
    
def trail4():
    global hour
    global distance
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
    hour = 4
    H = Label(go, text="Hour: " + str(hour), bg="#e6b8a0", fg="#843c3c")
    H.place(x=475, y=45)

    # Distance 
    distance = 50
    if distance >= 40:
        l = Label(go, text="Location: Graveyards Edge", bg="#e6b8a0", fg="#843c3c").place(x=450,y=65)

    # List of distractions (lose a group member)
    D = [' left to carve a pumpkin', ' joined Halloween festivities', ' got scared by a ghost', ' got scared by vampires']
    # List of misfourtunes (lose an hour)
    M = ["Zero lost his bone", "Sally's stitches ripped", "The Mayor lost his hat", "The Mummy Boy unraveled"]
    # Names of group members
    N = ['Zero', 'Sally', 'The Mayor', 'The Mummy Boy']
    # Random
    RM = random.randint(1,50)
    print(RM)
    if RM == 16:
        pause1 = Label(go, text= "Zero lost his bone", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 12:
        pause2 = Label(go, text= "Sally's stitches ripped", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour += 1
    elif RM == 3:
        pause3 = Label(go, text= "The Mayor lost his hat", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1
    elif RM == 23:
        pause4 = Label(go, text= "The Mummy Boy unraveled", fg ="#843c3c", bg="#e6b8a0").place(x=425, y=150)
        hour + 1


    # Energy (Uses Progress Bars)
    Progress = ttk.Progressbar(go, orient = HORIZONTAL, length = 100, mode = 'determinate', value=20).place(x=450,y=100)

    # Next 
    next = Button(go, text="Next", command=end).place(x=475,y=200)

def end():
    global hour
    global distance
    go = Toplevel()
    go.title('Oh No!')
    go.geometry('600x400')
    go.configure(bg="#e6b8a0")
    load = Image.open('facepalm.png')
    resize = load.resize((375, 275), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(resize) 
    img1 = Label(go, image=render)
    img1.image=render
    img1.place(x=0,y=0)  

    ohno = Label(go,text = "Nobody checked the supplies!\nRats ate all of the food\n and destroyed everything!", bg="#e6b8a0", fg="#843c3c").place(x=400, y=100)
   
    # Next 
    next = Button(go, text="Next", command=quit).place(x=475,y=200)

def checksupplies():
    new = Toplevel()
    new.geometry("600x400")
    new.configure(bg="#e6b8a0")
    load = Image.open('think.png')
    resize = load.resize((375, 275), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(resize) 
    img1 = Label(new, image=render)
    img1.image=render
    img1.place(x=0,y=0)  

    # Label 
    lb = Label(new, text='Oh No! \nSomeone forgot to pack!\nGuess we have to try again another day.', fg ="#843c3c", bg="#e6b8a0").place(x=380,y=50)
    # Button 
    no = Button(new, text="Quit", command=quit, fg ="#843c3c").place(x=475,y=200)
    

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
hour = 0 
distance = 50


win.mainloop()