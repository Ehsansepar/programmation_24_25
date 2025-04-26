# from tkinter import Tk, Label, Button
# from tkinter import *

# # fontions
# count = 0

# def button_click() :
#     global count
#     count += 1
#     counter.config(text=count)
#     reset_button.pack(padx=10)


# def button_reset() :
#     global count
#     count = 0
#     counter.config(text=count)


# ***************************************************


# window = Tk()
# window.geometry("520x500")
# window.title("Learning Camp")
# window.config(background="#2b2b2b")


#  *******************************************************


# label = Label(  window, 
#                 text="Hello this is a test", 
#                 bg="gray", 
#                 fg="white", 
#                 font=("Arial", 20),
#                 bd=1,
#                 relief="raised",
#                 padx=50,
#                 pady=20,
#                 # image=render,
#                 )
                
# # label.pack()
# label.pack(pady=20)

# counter = Label(window, 
#                 text="0",
#                 font=("Arial", 50),
#                 bg="#2b2b2b",
#                 fg="white")
# counter.pack(pady=30)

# button = Button(window,
#                 text="click me",
#                 bg="orange",
#                 fg="white", 
#                 font=("Arial", 20),
#                 command=button_click)
# button.pack(pady=20)

# reset_button = Button(window,
#                 text="reset",
#                 bg="red",
#                 fg="white", 
#                 font=("Arial", 20),
#                 command=button_reset)
# reset_button.pack(pady=20)

# window.mainloop()


#! -------------------------------------------------------------------------------------
        # intput_box

# from customtkinter import *

# def lightmode():
#     set_appearance_mode("dark")

# def submit(): 
#     username = entry.get()
#     if username:  # Vérifie si l'entrée n'est pas vide
#         clear.pack()  # Affiche le bouton Reset
#         # backspace.pack()
#     print("hello", username)

# def reset():
#     entry.delete(0, END)  # Correction: ajout des paramètres pour delete
#     clear.pack_forget()   # Cache le bouton Reset

# def backspace() :
#     entry.delete(len(entry.get())-1, END)

# set_appearance_mode("dark")
# app = CTk()

# entry = CTkEntry(app, 
#                 font=("Arial", 50), 
#                 bg_color="green", 
#                 fg_color="black", 
#                 width=350)
# entry.pack()

# submit = CTkButton(app, 
#                   text="Submit",
#                   font=("Arial", 20),
#                   fg_color="blue",
#                   hover_color="darkblue",
#                   command=submit)
# submit.pack()

# clear = CTkButton(app, 
#                   text="Reset",
#                   font=("Arial", 20),
#                   fg_color="blue",
#                   hover_color="darkblue",
#                   command=reset)

# backspace = CTkButton(app, 
#                   text="Backspace",
#                   font=("Arial", 20),
#                   fg_color="blue",
#                   hover_color="darkblue",
#                   command=backspace)
# backspace.pack()


# app.mainloop()

#! -------------------------------------------------------------------------------------

# frame in frame 


# from customtkinter import *


# app = CTk()
# app.geometry("630x500")

# # set_appearance_mode()
# # set_default_color_theme()

# main_frame = CTkFrame(app)
# main_frame.pack(padx=20, pady=20, fill="both")

# title_label = CTkLabel(main_frame, 
#                       text="Login / Sign up ",
#                       font=("Inter", 32, "bold"))
# title_label.pack(pady=20)


# login_button = CTkButton(main_frame,
#                         font=("Arial",20, "bold"),
#                         text="Login")
# login_button.pack(side="left", padx=100, pady=20)

# signup_button = CTkButton(main_frame,
#                         font=("Arial",20, "bold"),
#                         text="Sign up")
# signup_button.pack(side="left", padx=10, pady=20)

# # input
# input_frame = CTkFrame(main_frame)
# input_frame.pack(pady=10, padx=20, fill="both")

# username_input = CTkEntry(input_frame,
#                           width=350,
#                           height=50)
# username_input.pack(pady=10)

# password_input = CTkEntry(input_frame, 
#                           width=350,
#                           height=50)
# password_input.pack(pady=10)



# app.mainloop()

#! -------------------------------------------------------------------------------------

# from customtkinter import * # No longer needed
from ttkbootstrap import *
import ttkbootstrap as ttk

app = ttk.Window()
app.geometry("430x400")

button = ttk.Button(app, text="My Button", bootstyle="info") # Added text to the button
button.pack()

app.mainloop()