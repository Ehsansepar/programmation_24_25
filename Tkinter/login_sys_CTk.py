from customtkinter import *
from pathlib import Path

# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ehsan\Desktop\project\build\assets\frame0")

# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)

def login(): 
    username = entry_1.get()
    password = entry_2.get()

    # Cacher les anciens messages
    error_label.pack_forget()
    success_label.pack_forget()

    if username == "sepaehs" and password == "123":
        success_label.pack(pady=10)
    else:
        error_label.pack(pady=10)

set_appearance_mode("dark")
set_default_color_theme("blue")

app = CTk()
app.geometry("630x500")
app.title("Login System")

# Frame principal pour le contenu
main_frame = CTkFrame(app)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Titre
title_label = CTkLabel(main_frame, 
                      text="Login System",
                      font=("Inter", 32, "bold"))
title_label.pack(pady=20)

# Frame pour les entrées
input_frame = CTkFrame(main_frame)
input_frame.pack(pady=20, padx=20, fill="both")

# Username
username_label = CTkLabel(input_frame,
                         text="Username",
                         font=("Inter", 20))
username_label.pack(pady=(0, 5))fdsg

entry_1 = CTkEntry(input_frame,
                  width=340,
                  height=42,
                  font=("Arial", 20),
                  placeholder_text="Enter username")
entry_1.pack(pady=10)

# Password
password_label = CTkLabel(input_frame,
                         text="Password",
                         font=("Inter", 20))
password_label.pack(pady=(0, 5))

entry_2 = CTkEntry(input_frame,
                  width=340,
                  height=42,
                  font=("Arial", 20),
                  placeholder_text="Enter password",
                  show="*")
entry_2.pack(pady=10)

# Bouton de login
login_button = CTkButton(main_frame,
                        text="Login",
                        font=("Inter", 20, "bold"),
                        width=340,
                        height=42,
                        command=login)
login_button.pack(pady=20)

# Labels pour les messages de feedback
error_label = CTkLabel(main_frame,
                      text="Wrong username or password!",
                      text_color="red",
                      font=("Inter", 16))

success_label = CTkLabel(main_frame,
                        text="User logged in successfully!",
                        text_color="green",
                        font=("Inter", 16))

app.mainloop()
