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

# # from customtkinter import * # No longer needed
# from ttkbootstrap import *
# import ttkbootstrap as ttk

# app = ttk.Window()
# app.geometry("430x400")

# button = ttk.Button(app, text="My Button", bootstyle="info") # Added text to the button
# button.pack()

# app.mainloop()

#! -------------------------------------------------------------------------------------

# from customtkinter import *
# from tkinter import ANCHOR
# from PIL import Image
# import os

# # Get the directory of the current script
# current_dir = os.path.dirname(os.path.abspath(__file__))
# img_path = os.path.join(current_dir, 'Python-logo.png')
# img = Image.open(img_path)

# def theme_selection(choice):
#     if choice.lower() == "light":
#         set_appearance_mode("light")
#     else:
#         set_appearance_mode("dark")

# app = CTk()
# app.geometry("450x400")

# # Theme selector at the top
# select_theme = CTkComboBox(app, 
#                           values=["Light", "Dark"],
#                           command=theme_selection)
# select_theme.pack(pady=20)

# button = CTkButton(app, 
#                   text="Click Me",
#                   text_color="blue", 
#                   fg_color="transparent", 
#                   border_color="red",
#                   hover_color="blue",
#                   font=('Arial', 20),
#                   corner_radius=50,
#                   image=CTkImage(light_image=img, dark_image=img))
# button.place(anchor="center", relx=0.5, rely=0.5)

# app.mainloop()



# import customtkinter as ctk

# def add_task():
#     task = task_entry.get()
#     if task:
#         task_list.insert(ctk.END, f"• {task}\n")
#         task_entry.delete(0, ctk.END)

# def clear_tasks():
#     task_list.delete(1.0, ctk.END)

# # Create the main window
# app = ctk.CTk()
# app.geometry("400x500")
# app.title("Simple To-Do List")

# # Set appearance mode
# ctk.set_appearance_mode("light")

# # Title
# title_label = ctk.CTkLabel(app, text="My To-Do List", font=("Arial", 24))
# title_label.pack(pady=20)

# # Task entry
# task_entry = ctk.CTkEntry(app, placeholder_text="Enter a task", width=300)
# task_entry.pack(pady=10)

# # Add button
# add_button = ctk.CTkButton(app, text="Add Task", command=add_task)
# add_button.pack(pady=5)

# # Task list
# task_list = ctk.CTkTextbox(app, width=300, height=250)
# task_list.pack(pady=10)

# # Clear button
# clear_button = ctk.CTkButton(app, text="Clear All", command=clear_tasks, fg_color="#ff6b6b")
# clear_button.pack(pady=5)

# app.mainloop()


from customtkinter import *
from PIL import Image
task_count = 0
def task_submit() :
    global task_count
    task_text = task_entry.get()

    if task_text.strip() :
        task_count += 1
        task_list.insert(END, f"{task_count}. {task_text}\n")
        print("Task has been added succesfully !")
        task_entry.delete(0, END)

def delete_button_fonction(): 
    ...


# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, 'image_fx.jpg')
img = CTkImage(Image.open(img_path), size=(50, 50))  # Adjust size as needed

main_app = CTk()
main_app.title("To do Task")
main_app.geometry("550x500")

title_label = CTkLabel(main_app, 
                                           text="My to-do task",
                                           font=("Comic Sans MS", 30, "italic"),
                                           image=img,
                                           compound="left")  # Set the image to the left of the text
title_label.pack(padx=20, pady=(50, 0))

task_entry = CTkEntry(main_app, 
                                          placeholder_text="Enter Your task here !", 
                                          width=400,
                                          height=50,
                                          border_color="white",
                                          corner_radius=50,
                                          font=("Comic Sans MS", 20, "italic"))
task_entry.pack(padx=20, pady=(20, 0))

task_list = CTkTextbox(main_app, width=400, corner_radius=50,
                                           font=("Comic Sans MS", 20, "italic"),
                                           wrap="none", padx=0, pady=0, 
                                           spacing3=5)  # Adjust spacing3 for line padding
task_list.pack(padx=20, pady=(20, 0))

entryNumber_delete_task = CTkEntry(main_app, 
                                   placeholder_text="Enter task number to delete", 
                                   width=400,
                                   height=50,
                                   border_color="white",
                                   corner_radius=50,
                                   font=("Comic Sans MS", 20, "italic"))
# Don't use pack/grid/place initially if you want it hidden

# Pack the entry field defined earlier
# entryNumber_delete_task.pack(pady=(10, 0))

# Create a frame to hold both buttons side-by-side
# Use a transparent background to blend with the main window
button_frame = CTkFrame(main_app, fg_color="transparent")
# Use padding for the frame
button_frame.pack(pady=(25, 0))

# Define the submit button but don't pack it yet
submit_button = CTkButton(button_frame, text="Submit",
                          font=("Arial", 25),
                          corner_radius=50,
                          command=task_submit)
# Pack the submit button inside the frame, to the left
submit_button.pack(side="left", padx=10)

# Create the new delete button inside the frame
delete_button = CTkButton(button_frame, text="Delete Task",
                          font=("Arial", 25),
                          corner_radius=50,
                          fg_color="#ff6b6b",       # A reddish color for delete action
                          hover_color="#e05252",
                          command=delete_button_fonction)   # A darker red for hover effect
# Pack the delete button next to the submit button in the frame
delete_button.pack(in_=button_frame, side="left", padx=10)

main_app.mainloop()