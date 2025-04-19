# from tkinter import Tk, Label, Button
from tkinter import *

# fontions
count = 0

def button_click() :
    global count
    count += 1
    counter.config(text=count)
    reset_button.pack(padx=10)


def button_reset() :
    global count
    count = 0
    counter.config(text=count)


#! ***************************************************


window = Tk()
window.geometry("520x500")
window.title("Learning Camp")
window.config(background="#2b2b2b")


#! *******************************************************


label = Label(  window, 
                text="Hello this is a test", 
                bg="gray", 
                fg="white", 
                font=("Arial", 20),
                bd=1,
                relief="raised",
                padx=50,
                pady=20,
                # image=render,
                )
                
# label.pack()
label.pack(pady=20)

counter = Label(window, 
                text="0",
                font=("Arial", 50),
                bg="#2b2b2b",
                fg="white")
counter.pack(pady=30)

button = Button(window,
                text="click me",
                bg="orange",
                fg="white", 
                font=("Arial", 20),
                command=button_click)
button.pack(pady=20)

reset_button = Button(window,
                text="reset",
                bg="red",
                fg="white", 
                font=("Arial", 20),
                command=button_reset)
reset_button.pack(pady=20)

window.mainloop()