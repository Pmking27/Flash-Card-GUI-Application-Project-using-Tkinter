BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

try:
    data=pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:    
    original_data=pandas.read_csv("data/french_words.csv")
    original_data=pandas.read_csv("data/french_words.csv")
    to_data=original_data.to_dict(orient="records")
else:
    to_data=data.to_dict(orient="records")

current_card={}

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=card_front_img)
    flip_timer=window.after(3000, func=filp_card)
    

def filp_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)

def is_known():
    to_data.remove(current_card)
    data=pandas.DataFrame(to_data)
    data.to_csv("data/word_to_learn.csv",index=False)
    next_card()

window=Tk()
window.resizable(0,0)
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.iconbitmap("images/flash_card_icon.ico")
flip_timer=window.after(3000, func=filp_card)


canvas=Canvas(width=800,height=526)
card_front_img=PhotoImage(file="C:/Users/admin/Desktop/my #100dayscodewithpython/Day 31 - Flash Card App Capstone Project/images/card_front.png")
card_back_img=PhotoImage(file="C:/Users/admin/Desktop/my #100dayscodewithpython/Day 31 - Flash Card App Capstone Project/images/card_back.png")
card_bg=canvas.create_image(400,263,image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(390,100,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(390,250,text="",font=("Ariel",60,"bold"))

cross_image=PhotoImage(file="images/wrong.png")
unknown_button =Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)

check_image=PhotoImage(file="images/right.png")
known_button =Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(column=1,row=1)

next_card()

window.mainloop()