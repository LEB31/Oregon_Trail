# Lily Bain  Oregon Trail  Version 1.5
# Credit to Codemy.com for assistance on the tkinter canvas, www.tutorialspoint.com, geeksforgeeks.com, pythontutorial.net
from tkinter import * 
from tkinter import PhotoImage  
from PIL import Image, ImageTk
import tkinter as ttk 
import random 
# win is short for window 
win= Tk() 
win.title('The Oregon Trail')
win.geometry("635x400") 

load = Image.open('IM.png')
resize = load.resize((275, 175), Image.ANTIALIAS)
render = ImageTk.PhotoImage(resize)
img = Label(win, image=render)
img.place(x=0,y=0)

#Misc. Variables & lists
m = 850.00 #This is the amount of money you have     
total = 0

crew = ["John", "Sue", "Bob", "Ava", "Everyone", "John", "Sue", "Bob", "Ava", "John", "Sue", "Bob", "Ava"] 
DT = 0  #This is the days traveled
mis = ['measles', 'a snakebite', 'exhaustion', 'typhoid', 'cholera', 'dysentery','an infection'] 
s = 1 #This is equal to the stage of the game the user is on   


#Functions 
def delete(): 
  global s
  s + 1  
  occupation.destroy() 
  chk1.destroy()
  chk2.destroy()
  chk3.destroy() 
  chk4.destroy() 
  select1.destroy()  
  stage3()

def stage3():   
  Month.place(x=355,y=70) 
  P.place(x=350,y=30)
  March.place(x=390,y=105) 
  April.place(x=390,y=125) 
  May.place(x=390,y=145) 
  June.place(x=390,y=165) 
  July.place(x=390,y=185) 
  select2.place(x=395,y=215)

def stage4(): 
  Month.destroy() 
  P.destroy()
  March.destroy()
  April.destroy() 
  May.destroy()
  June.destroy()
  July.destroy()
  select2.destroy() 
  Money.place(x=330,y=30)  
  party.place(x=290,y=55) 
  shop.place(x=330,y=80) 
  shop1.place(x=390,y=110) 

def stage5(): 
  Money.destroy() 
  party.destroy() 
  shop.destroy() 
  shop1.destroy()   
  Money2.place(x=375,y=80) 
  shopName.place(x=315, y=30) 
  bonus.place(x=350, y=55) 
  order.place(x=350, y=105)    
  Yoke2.place(x=310, y=130) 
  Yoke.place(x=290, y=155)
  yoke.place(x=515,y=153)  
  buy.place(x=555, y=150)  
  pf.place(x=300, y=180)
  Food.place(x=245, y=205) 
  food.place(x=530, y=200) 
  buyc.place(x=570, y=197) 
  c.place(x= 350,  y=225) 
  AC.place(x=310,y=245) 
  clothes.place(x=525, y=244) 
  buyC.place(x=565, y=243) 
  store.place(x=350, y=275)

def S():  
  cy = 40.00
  y = yoke.get()  
  y = int(y) 
  m1 = m - (y * cy)
  if y <= 5:  
    m3 = Label(win,text=f'You Have ${m1} Left') 
    m3.place(x=75, y=180)
  cf = 0.20 
  f = food.get() 
  f = int(f)   
  m2 = m1 - (f * cf)
  if f <= 200: 
    fm = Label(win,text=f"You Have ${m2}")  
    m3.destroy()
    fm.place(x=75, y=180)
  cc = 10.00 
  c = clothes.get()  
  c = int(c)  
  global m4
  m4 = m2 - (c * cc)
  if c <= 20: 
    cm = Label(win,text=f"You Have ${m4}") 
    cm.place(x=75, y=180)  
  global total 
  total = m4
  
  
def S1(): 
  Money2.destroy() 
  shopName.destroy() 
  bonus.destroy()
  order.destroy()   
  Yoke2.destroy()
  Yoke.destroy()
  yoke.destroy() 
  buy.destroy()
  pf.destroy()
  Food.destroy()
  food.destroy()
  buyc.destroy() 
  c.destroy()
  AC.destroy()
  clothes.destroy()
  buyC.destroy()  
  sn2.place(x=350,y=30)  
  store.destroy()  
  w.place(x=300,y=50) 
  wp.place(x=385,y=75) 
  wh.place(x=385,y=105) 
  wa.place(x=385,y=135) 
  wt.place(x=385,y=165) 
  wheel.place(x=500,y=105) 
  axel.place(x=500,y=135) 
  tongue.place(x=500,y=165) 
  buyw.place(x=545,y=100) 
  buya.place(x=545,y=130) 
  buyt.place(x=545,y=160)   
  checkout.place(x=380,y=200)

def S2():  
  global total   
  W = wheel.get() 
  W = int(W)
  a = axel.get() 
  a = int(a)
  t = tongue.get() 
  t = int(t)  
  m5 = total 
  if W <= 3 or a <= 3 or t <=3:  
    m6 = m5 - ((W + a + t) * 10) 
    M5 = Label(win, text=f'You Have ${m6} Left') 
    M5.place(x=75,y=180)  
  

def check():   
  sn2.destroy() 
  store.destroy()  
  w.destroy() 
  wp.destroy() 
  wh.destroy() 
  wa.destroy() 
  wt.destroy() 
  wheel.destroy()  
  axel.destroy() 
  tongue.destroy() 
  buyw.destroy() 
  buya.destroy() 
  buyt.destroy()    
  checkout.destroy()  
  global total  
  j.place(x=375,y=75) 
  jn.place(x=400,y=150) 

def start():   
  j.destroy() 
  jn.destroy() 
  top = Toplevel()  
  top.geometry("635x400") 
  top.title("Day 1")  
  top.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top, image=render)
  img1.image=render
  img1.place(x=0,y=0)  
  day = Label(top,text=f'Day #{DT + 1}')
  day.place(x=410, y=5)    
  dw = Label(top,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top,text="Weather: ") 
  dw1.place(x=400,y=30) 
  mis = ['measles', 'a snakebite', 'exhaustion', 'typhoid', 'cholera', 'dysentery','an infection'] 
  crew = ["John", "Sue", "Bob", "Ava", "Everyone", "John", "Sue", "Bob", "Ava", "John", "Sue", "Bob", "Ava"]  
  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top,text="Health: ") 
  dh1.place(x=400,y=45)  
  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14: 
    dm = Label(top,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
      

  dis = Label(top,text='102 miles till Kansas River Crossing')  
  dis.place(x=350,y=75) 
  ND = Button(top, text='Continue',command = Day2) 
  ND.place(x=400,y=100)  
  
def Day2(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 2")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  Day = 2
  day = Label(top1,text=f'Day #{Day}')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  
  
  dis = Label(top1,text='84 miles till Kansas River Crossing')  
  dis.place(x=350,y=75) 
  ND = Button(top1, text='Continue',command = Day3) 
  ND.place(x=400,y=100)   


def Day3(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 3")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  Day = 3
  day = Label(top1,text=f'Day #{Day}')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text=f'67 miles till Kansas River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

  ND = Button(top1, text='Continue',command = Day4) 
  ND.place(x=400,y=100)   

def TE(): 
  ten = Toplevel() 
  ten.geometry("635x400") 
  ten.title("GAME OVER") 
  TE = Label(ten,text='Lightning has Struck the Wagon\n    GAME OVER')  
  TE.place(x=225,y=150) 
  teb = Button(ten,text='END', command = click) 
  teb.place(x=300,y=225)

def click(): 
  exit()

def Day4(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 4")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  

  day = Label(top1,text='Day #4')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text='42 miles till Kansas River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

  ND = Button(top1, text='Continue',command = Day5) 
  ND.place(x=400,y=100)   


def Day5(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 5")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #5')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text=f'23 miles till Kansas River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

  ND = Button(top1, text='Continue', command = Day6) 
  ND.place(x=400,y=100)    

def Day6(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 6")  
  top1.configure(bg='green')
  load = Image.open('KRC.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #6')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  
  KRC = Label(top1,text='Welcome to the Kansas River Crossing') 
  KRC.place(x=220,y=200) 
  krc1 = Label(top1,text='You can Either try and Cross the River, or Wait for a Ferry')
  krc1.place(x=190,y=235) 
  krcb1 = Button(top1,text='Attempt to\n Cross',command = Riva) 
  krcb1.place(x=215,y=275)
  krcb2 = Button(top1,text='Wait for Ferry',command = ferry) 
  krcb2.place(x=425,y=275)
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

    

def Riva():  
  top1 = Toplevel() 
  top1.geometry("635x400")  
  top1.configure(bg='green')
  top1.title("Attempt to Cross") 
  load = Image.open('KRC.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)  
  L = random.randint(1,2)  
  if L == 1: 
    live = Label(top1,text='You Have Sucessfully Crossed the River')  
    live.place(x=360,y=75)
    liveb = Button(top1,text='Continue',command = ferry) 
    liveb.place(x=350,y=105)
  elif L ==2:
   d = Label(top1,text='Your Wagon Sunk in the River\n   GAME OVER') 
   d.place(x=350,y=50) 
   db = Button(top1,text='END',command = click) 
   db.place(x=425,y=100)

def ferry(): 
  top1 = Toplevel() 
  top1.geometry("635x400")  
  top1.configure(bg='green')
  top1.title("On the Trail") 
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  B = Label(top1, text='You are 82 miles from the Big Blue River Crossing') 
  B.place(x=295,y=75)
  day = Label(top1,text='Day #7')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

  ND = Button(top1, text='Continue', command = Day8) 
  ND.place(x=400,y=100)    

def Day8(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 8")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #8')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text='You are 63 miles away from the\n Big Blue River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()

  ND = Button(top1, text='Continue', command = Day9) 
  ND.place(x=400,y=125)    

def Day9(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 9")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #9')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text='You are 47 miles away from the\n Big Blue River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()
  
  rand_value4 = int(random.random() * len(crew)-1)
  cd2 = (crew[rand_value4]) 
  rn = random.randint(1,len(crew)-1) 
  if rn == 0: 
    cd3 = Label(top1,text=f'{cd2} has died')
    crew.remove(cd2) 
    

  ND = Button(top1, text='Continue', command = Day10) 
  ND.place(x=400,y=125)    

def Day10(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 10")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #10')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text='You are 25 miles away from the\n Big Blue River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()
  
  rand_value4 = int(random.random() * len(crew)-1)
  cd2 = (crew[rand_value4]) 
  rn = random.randint(1,len(crew)-1) 
  if rn == 0: 
    cd3 = Label(top1,text=f'{cd2} has died')
    crew.remove(cd2) 
    

  ND = Button(top1, text='Continue',command = Day11) 
  ND.place(x=400,y=125)    

def Day11(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 11")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #11')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  dis = Label(top1,text='Welcome to the Big Blue River Crossing')  
  dis.place(x=350,y=75)
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()
  
  rand_value4 = int(random.random() * len(crew)-1)
  cd2 = (crew[rand_value4]) 
  rn = random.randint(1,len(crew)-1) 
  if rn == 0: 
    cd3 = Label(top1,text=f'{cd2} has died')
    crew.remove(cd2) 
    
  krc1 = Label(top1,text='You can Either try and Cross the River, or Wait for a Ferry')
  krc1.place(x=190,y=235) 
  krcb1 = Button(top1,text='Attempt to\n Cross',command = BBRC) 
  krcb1.place(x=215,y=275)
  krcb2 = Button(top1,text='Wait for Ferry',command = Day13) 
  krcb2.place(x=425,y=275)
     

def BBRC(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Attempt to Cross")  
  top1.configure(bg='green')
  load = Image.open('BBRC.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)  
  L = random.randint(1,2) 
  if L == 1: 
    live = Label(top1,text='You Have Sucessfully Crossed the River')  
    live.place(x=360,y=75)
    liveb = Button(top1,text='Continue',command = Day13) 
    liveb.place(x=350,y=105)
  elif L ==2:
   d = Label(top1,text='Your Wagon Sunk in the River\n   GAME OVER') 
   d.place(x=350,y=50) 
   db = Button(top1,text='END',command = click) 
   db.place(x=425,y=100)
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()
  
  rand_value4 = int(random.random() * len(crew)-1)
  cd2 = (crew[rand_value4]) 
  rn = random.randint(1,len(crew)-1) 
  if rn == 0: 
    cd3 = Label(top1,text=f'{cd2} has died')
    crew.remove(cd2) 

def Day13(): 
  top1 = Toplevel() 
  top1.geometry("635x400") 
  top1.title("Day 12")  
  top1.configure(bg='green')
  load = Image.open('trail.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(top1, image=render)
  img1.image=render
  img1.place(x=0,y=0)    
  
  day = Label(top1,text='Day #12')
  day.place(x=410, y=5)     

  dw = Label(top1,text='')
  weather = ['cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot', 'cool', 'cold', 'warm', 'hot']   
  rand_value = int(random.random() * len(weather)-1) 
  answer = (weather[rand_value]) 
  dw.config(text=answer)
  dw.place(x=470,y=30) 
  dw1 = Label(top1,text="Weather: ") 
  dw1.place(x=400,y=30)   

  health = ["good","average",'poor','perfect',"good","average",'poor','perfect',"good","average",'poor','perfect']  
  dh = Label(top1,text='')
  rand_value1 = int(random.random() * len(health)-1) 
  answer1 = (health[rand_value1]) 
  dh.config(text=answer1)
  dh.place(x=455,y=45) 
  dh1 = Label(top1,text="Health: ") 
  dh1.place(x=400,y=45)   

  RM = random.randint(1,100)   
  if RM == 94 or RM == 40 or RM == 29 or RM == 35 or RM == 59 or RM == 24 or RM == 19 or RM == 65 or RM == 80 or RM == 4 or RM == 41 or RM ==14:  
    dm = Label(top1,text='')
    rand_value2 = int(random.random() * len(mis)-1) 
    answer2 = (mis[rand_value2]) 
    dm.config(text=answer2)
    dm.place(x=465,y=165) 
    dm1 = Label(top1,text="has") 
    dm1.place(x=435,y=165)  
    mc = Label(top1,text='')
    rand_value3 = int(random.random() * len(crew)-1) 
    answer3 = (crew[rand_value3]) 
    mc.config(text=answer3)
    mc.place(x=400,y=165) 
  
  
  TEN = random.randint(1,25) 
  while TEN == 5:   
    TE()
  
  rand_value4 = int(random.random() * len(crew)-1)
  cd2 = (crew[rand_value4]) 
  rn = random.randint(1,len(crew)-1) 
  if rn == 0: 
    cd3 = Label(top1,text=f'{cd2} has died')
    crew.remove(cd2) 
    

  ND = Button(top1, text='Continue',command = ending) 
  ND.place(x=400,y=125) 

def ending(): 
  END = Toplevel() 
  END.geometry("635x400") 
  END.title("END")  
  END.configure(bg='green')
  load = Image.open('T.png')
  resize = load.resize((275, 175), Image.ANTIALIAS)
  render = ImageTk.PhotoImage(resize) 
  img1 = Label(END, image=render)
  img1.image=render
  img1.place(x=0,y=0)  
  d = Label(END,text='In the Middle of the Night,\nthe Wagon was Attacked by Bandits') 
  d.place(x=350,y=25) 
  d1 = Label(END,text='There are no Survivors') 
  d1.place(x=400,y=65) 
  b1 = Button(END,text='END', command = click) 
  b1.place(x=450,y=100)

#widgets before the trail starts
welcome = Label(win, text='Welcome to the Oregon Trail!') 
occupation = Label(win, text='Please Select a Job Below:')   
Money = Label(win, text=f"You Have Saved $800 for This Trip") 
Money2 = Label(win, text=f"You Have ${m}",fg='dark green')
Month = Label(win, text='Which Month Would you\n Like to Leave in?') 
P = Label(win, text="The Year is 1848 and you\n are in Independence, Missouri") 
party = Label(win, text="John, Sue, Bob, and Ava have decided to join you",fg="dark green") 
shop = Label(win, text="You might want to shop before you go") 
shopName = Label(win, text="You Have Entered Mr.Webb's General Store",fg='dark green') 
bonus = Label(win, text="He Gives you a Bonus $50!")
order = Label(win, text= "What Would you Like to Buy?") 
Yoke = Label(win, text='How Many Yokes Would you Like?',fg="dark green") 
Yoke2 = Label(win, text='There are 2 Oxen in a Yoke, $40 for a Yoke')    
pf = Label(win, text='A Pound of Food Costs 20 Cents per Pound')
Food = Label(win, text='How Many Pounds of Food Would you Like?',fg="dark green")  
c = Label(win,text='A set of Clothes Cost $10')
AC = Label(win,text='How Many sets Would you Like?',fg="dark green") 
sn2 = Label(win,text='You are in the Back of the Store') 
A = Label(win,text='Here is What you Found') 
w = Label(win,text='Wagon Wheels, Axels, and Tongues are $10 each',fg='dark green') 
wp = Label(win,text='What Would you Like?') 
wh = Label(win,text="Wagon Wheels",fg='dark green') 
wa = Label(win,text="Wagon Axels",fg="dark green") 
wt = Label(win,text='Wagon Tongues',fg="dark green") 
j = Label(win, text="Let's get Started!",fg="dark green")

March = Checkbutton(win, text="March") 
April = Checkbutton(win, text="April") 
May = Checkbutton(win, text="May") 
June =Checkbutton(win, text="June") 
July = Checkbutton(win, text="July")   
chk1 = Checkbutton(win, width=15, text='Farmer')
chk2 = Checkbutton(win, width=15, text='Candle Maker') 
chk3 = Checkbutton(win, width=15, text='Wood Worker') 
chk4 = Checkbutton(win, width=15, text='Butcher') 

select1 = Button(win,text='Select', command=delete)  
select2 = Button(win,text='Select', command=stage4)  
shop1 = Button(win, text="Go to the\nGeneral Store", command=stage5)  
buy = Button(win, text='Buy', command=S) 
buyc = Button(win,text='Buy', command=S) 
buyC = Button(win,text="Buy", command=S) 
store = Button(win, text="Go Further Into the Store",command=S1) 
buyw = Button(win,text='Buy',command=S2) 
buya = Button(win,text='Buy',command=S2) 
buyt = Button(win,text='Buy',command=S2)  
#b = Button(win,text="Go to the Front of the Store",command=stage5) 
checkout = Button(win,text="Checkout Items",command=check) 
jn = Button(win,text="START",command=start)

yoke = Spinbox(win, from_=0, to=5, width=3)
food = Spinbox(win, from_=0, to=200, width=3) 
clothes = Spinbox(win, from_=0, to=20, width=3) 
wheel = Spinbox(win, from_=0, to=3, width=3) 
axel = Spinbox(win, from_=0, to=3, width=3) 
tongue = Spinbox(win, from_=0, to=3, width=3) 

#main code testing
 
welcome.place(x=350,y=5) 
occupation.place(x=350,y=25) 
chk1.place(x=330,y=45) 
chk2.place(x=350,y=65) 
chk3.place(x=349,y=85) 
chk4.place(x=330,y=105) 
select1.place(x=395,y=130)  

win.mainloop()