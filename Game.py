import tkinter as tk
from tkinter import *
import random
window=tk.Tk()
window.title("Game ")
window.geometry("700x600")

bg_color = "#87CEFA"  
button_color = "#4CAF50"
button_hover_color = "#45a049"
text_color = "#000000"


button_font = ('Arial', 15)
label_font = ('Times New Roman', 20)
option=("Rock","Paper","Scissors")

def Rb():
    Show_label.config(text="Rock")
    computer=random.choice(option)
    Show_label2.config(text=computer)
    Result()

def paper():
    Show_label.config(text="Paper")
    computer=random.choice(option)
    Show_label2.config(text=computer)
    Result()
   


def Scissors():
    Show_label.config(text="Scissors")
    computer=random.choice(option)
    Show_label2.config(text=computer)
    Result()

def Rematch():
    Result=""
    Show_label.config(text=Result)
   
    Show_label2.config(text=Result)
    ResultL.config(text=Result)

def Result():
    user_choice = Show_label.cget("text")
    computer_choice = Show_label2.cget("text")

    if user_choice == computer_choice:
        ResultL.config(text="Tie")
    elif (user_choice == "Rock" and computer_choice == "Scissors") :
         ResultL.config(text="You Win!")
    elif(user_choice == "Paper" and computer_choice == "Rock") :
         ResultL.config(text="You Win!")
    
    elif (user_choice == "Scissors" and computer_choice == "Paper"):
         ResultL.config(text="You Win!")
    else:
        ResultL.config(text="You Lose!")

label=tk.Label(text="** R.P.S GAME **",font=('Times New Roman',30), bg=bg_color, fg=text_color)
label.pack()

label2=tk.Label(text="-------------------------",font=('Times New Roman',30), bg=bg_color, fg=text_color)
label2.pack()

Select=tk.Label(text="Selected Option ",font=('Times New Roman',25), bg=bg_color, fg=text_color)
Select.place(x=20,y=100)

Computer=tk.Label(text="Computer",font=('Times New Roman',25), bg=bg_color, fg=text_color)
Computer.place(x=500,y=100)

Show_label=tk.Label(font=('Times New Roman',15), bg=bg_color, fg=text_color)
Show_label.place(x=50,y=200)

Show_label2=tk.Label(font=('Times New Roman',15), bg=bg_color, fg=text_color)
Show_label2.place(x=500,y=200)

ResultL=tk.Label(font=('Times New Roman' ,30), bg=bg_color, fg=text_color)
ResultL.place(x=240,y=300)

Rb=Button(window, text="Rock", width=8, height=4, font=('Arial', 15),bg=button_color, activebackground=button_hover_color,command=Rb)
Rb.place(x=50,y=400)

S_B=Button(window,text="Scisssors",width=8,height=4,font=('Arial',15),bg=button_color, activebackground=button_hover_color,command=Scissors)
S_B.place(x=175,y=400)
Pb=Button(window,text="Paper",width=8,height=4,font=('Arial',15),bg=button_color, activebackground=button_hover_color,command=paper)
Pb.place(x=300,y=400)

Rematch_b=Button(window,text="Rematch",width=8,height=4,font=('Arial',15),bg=button_color, activebackground=button_hover_color,command=Rematch)
Rematch_b.place(x=425,y=400)
ex=Button(window,text="Exit",width=8,height=4,font=('Arial',15),bg=button_color, activebackground=button_hover_color,command=exit)
ex.place(x=550,y=400)

window.configure(bg=bg_color)

window.mainloop()