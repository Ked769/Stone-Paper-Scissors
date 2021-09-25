from tkinter import *
import tkinter as tk
  
# creating tkinter window
root = Tk()
root.config(height = 640,width = 850)
root.pack_propagate(False)
root.resizable(0,0)
can = Canvas(root,bg='black',height=5000,width=5000)
can.place(relx=0.5,rely=0.5,anchor=CENTER)

#Importing Pictures

import os

cwd = os.getcwd()

print(cwd)

rock = cwd + "\\Resources\\imgs\\Rock.png"

paper = cwd + "\\Resources\\imgs\\paper.png"

scissors = cwd + "\\Resources\\imgs\\scissors.png"

icon=PhotoImage(file = "icon.png")

# Changing The Title
root.title("Rock Paper Scissors!")
  
# Adding widgets to the root window
title = Label(root, text = 'Rock Paper Scissors!\nChoose Your Weapon!', font =('Verdana', 15)).pack(side = TOP, pady = 10)
ico = Label(can, image=icon, text = "Rock Paper Scissors").pack(side=TOP)
  
# Creating a photoimage object to use image
rock_ph = PhotoImage(file = rock)

paper_ph = PhotoImage(file = paper)

scissors_ph = PhotoImage(file = scissors)
import random

#get the result
results = ["Win - Opponent Chose : ","Lose - Opponent Chose : ", "Tie - Opponent Chose : "]
arr = [0,1,2]
winLose = random.choice(arr)
compChoice = random.choice(results)
def paper():
    print("Paper!")
    global winLose
    global results
    global arr
    winLose = random.choice(arr)
    if winLose == 1:
        result = results[0] + "Rock"
    elif winLose == 2:
        result = results[1] + "Scissors"
    else:
        result = results[2] + "Paper"
    print(result)
    winLose = random.choice(arr)
    Res(result)
def rock():
    print("Rock!")
    global winLose
    global results
    if winLose == 1:
        result = results[0] + "Scissors"
    elif winLose == 2:
        result = results[1] + "Paper"
    else:
        result = results[2] + "Rock"
    print(result)
    winLose = random.choice(arr)
    Res(result)
def scissors():
    print("Scissors!")
    global winLose
    global results
    if winLose == 1:
        result = results[0] + "Paper"
    elif winLose == 2:
        result = results[1] + "Rock"
    else:
        result = results[2] + "Scissors"
    print(result)
    winLose = random.choice(arr)
    Res(result)
def Res(x):
    resultWin = Tk()
    resultWin.config(height = 50, width = 300)
    resultWin.resizable(0,0)
    resultWin.pack_propagate(False)
    resultWin.title("Rock..Paper..Scissors..Shoot!")
    xs = Label(resultWin,text = x).pack()
    resultWin.mainloop()
    
# Here, image option is used to
# set image on button
scissors = tk.Button(can, text = 'Scissors', image = scissors_ph,command=scissors)
scissors.pack(side=RIGHT)
paper = tk.Button(can, text = 'Paper', image = paper_ph,command=paper)
paper.pack(side=RIGHT)
rock = tk.Button(can, text = 'Rock', image = rock_ph,command=rock)
rock.pack(side=RIGHT)

mainloop()
