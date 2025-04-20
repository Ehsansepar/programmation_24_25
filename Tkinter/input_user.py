from customtkinter import *

def lightmode():
    set_appearance_mode("dark")

def submit(): 
    username = entry.get()
    if username:  # Vérifie si l'entrée n'est pas vide
        clear.pack()  # Affiche le bouton Reset
        # backspace.pack()
    print("hello", username)

def reset():
    entry.delete(0, END)  # Correction: ajout des paramètres pour delete
    clear.pack_forget()   # Cache le bouton Reset

def backspace() :
    entry.delete(len(entry.get())-1, END)

set_appearance_mode("dark")
app = CTk()

entry = CTkEntry(app, 
                font=("Arial", 50), 
                bg_color="green", 
                fg_color="black", 
                width=350)
entry.pack()

submit = CTkButton(app, 
                  text="Submit",
                  font=("Arial", 20),
                  fg_color="blue",
                  hover_color="darkblue",
                  command=submit)
submit.pack()

clear = CTkButton(app, 
                  text="Reset",
                  font=("Arial", 20),
                  fg_color="blue",
                  hover_color="darkblue",
                  command=reset)

backspace = CTkButton(app, 
                  text="Backspace",
                  font=("Arial", 20),
                  fg_color="blue",
                  hover_color="darkblue",
                  command=backspace)
backspace.pack()


app.mainloop()