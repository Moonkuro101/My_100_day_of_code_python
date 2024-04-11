from tkinter import *
import sys
import pandas as pd
import random as rn
BACKGROUND_COLOR = "#B1DDC6"
EN = "English"
TH = "Thai"

try:
    the_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    the_words = pd.read_csv("data/English_words.csv")
    
the_words_dict = the_words.to_dict(orient="records")

def stop():
    word_to_learn = pd.DataFrame(the_words_dict) 
    word_to_learn.to_csv("data/words_to_learn.csv",index=False)
    sys.exit()

def next_card():
    global choice,time
    window.after_cancel(time)
    choice = rn.choice(the_words_dict)
    canvas.itemconfig(word_canva,text=choice["English"],fill="Black")
    canvas.itemconfig(language_canvas,text="English",fill="Black")
    canvas.itemconfig(imgs,image=Card_f)
    time = window.after(3000,back_card)

def know():
    the_words_dict.remove(choice)
    next_card()

def back_card():
    canvas.itemconfig(language_canvas,text="ไทย",fill="White")
    canvas.itemconfig(imgs,image=Card_b)
    canvas.itemconfig(word_canva,text=choice["Thai"],fill="White")

   

window = Tk()
time = window.after(0)
window.title("Flash Card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=562)
Card_f = PhotoImage(file='./images/card_front.png')
Card_b = PhotoImage(file='./images/card_back.png')
imgs = canvas.create_image(400,263,image=Card_f)

canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
language_canvas = canvas.create_text(400,150,text="English",font=("Ariel",40,"italic"))
word_canva = canvas.create_text(400,263,text=f"Word",font=("Ariel",60,"bold"))


image_Y = PhotoImage(file="./images/right.png")
button_correct = Button(image=image_Y, highlightthickness=0,command=know)
button_correct.grid(row=1,column=1)

image_x = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_x, highlightthickness=0,command=next_card)
button_wrong.grid(row=1,column=0)

button_correct = Button(text="Stop",highlightthickness=0,command=stop,font=("Ariel",60,"bold"))
button_correct.grid(row=1,column=2)

time = window.after(3000,back_card)
next_card()



window.mainloop()
