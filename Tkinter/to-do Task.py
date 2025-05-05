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
    global task_count
    entryNumber_delete_task.pack()
    num_to_delete_str = entryNumber_delete_task.get()

    if not num_to_delete_str.isdigit():
        entryNumber_delete_task.delete(0, END)
        return

    num_to_delete = int(num_to_delete_str)

    all_tasks_text = task_list.get("1.0", "end-1c")
    task_lines = [line for line in all_tasks_text.splitlines() if line.strip()]

    if not (1 <= num_to_delete <= len(task_lines)):
        entryNumber_delete_task.delete(0, END)
        return

    # Remove the task using list index (task number - 1)
    del task_lines[num_to_delete - 1]

    task_count = len(task_lines)

    task_list.delete("1.0", END)

    new_list_content = []
    for i, task_line in enumerate(task_lines):
        # Get the task text after the first '.'
        try:
            task_text = task_line.split('.', 1)[1].strip()
        except IndexError: # If line format is unexpected
            task_text = task_line.strip()
        # Add back with new number
        new_list_content.append(f"{i + 1}. {task_text}")

    # Put the renumbered list back
    if new_list_content:
        task_list.insert("1.0", "\n".join(new_list_content) + "\n")

    entryNumber_delete_task.delete(0, END)


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

# ------------------------------------------------------------------------------------------------------------------

# main_app.py
import customtkinter as ctk
from PIL import Image
import os

# --- Variables Globales ---
app = None  # Fenêtre principale
login_frame = None
todo_frame = None
task_entry = None
task_list = None
entryNumber_delete_task = None
task_count = 0


# --- Fonctions de la liste de tâches (adaptées de to-do Task.py) ---
def task_submit():
    global task_count, task_list, task_entry
    task_text = task_entry.get()
    if task_text.strip():
        task_count += 1
        task_list.insert(ctk.END, f"{task_count}. {task_text}\n")
        print("Task has been added successfully!")
        task_entry.delete(0, ctk.END)

def delete_button_fonction():
    global task_count, task_list, entryNumber_delete_task
    entryNumber_delete_task.pack(pady=(10, 5)) # Afficher le champ si ce n'est pas déjà fait
    num_to_delete_str = entryNumber_delete_task.get()

    if not num_to_delete_str.isdigit():
        print("Please enter a valid number.")
        entryNumber_delete_task.delete(0, ctk.END)
        return

    num_to_delete = int(num_to_delete_str)
    all_tasks_text = task_list.get("1.0", "end-1c")
    task_lines = [line for line in all_tasks_text.splitlines() if line.strip()]

    if not (1 <= num_to_delete <= len(task_lines)):
        print("Invalid task number.")
        entryNumber_delete_task.delete(0, ctk.END)
        return

    del task_lines[num_to_delete - 1]
    task_count = len(task_lines)
    task_list.delete("1.0", ctk.END)

    new_list_content = []
    for i, task_line in enumerate(task_lines):
        try:
            task_text = task_line.split('.', 1)[1].strip()
        except IndexError:
            task_text = task_line.strip()
        new_list_content.append(f"{i + 1}. {task_text}")

    if new_list_content:
        task_list.insert("1.0", "\n".join(new_list_content) + "\n")

    entryNumber_delete_task.delete(0, ctk.END)
    entryNumber_delete_task.pack_forget() # Cacher à nouveau le champ après suppression
    print("Task deleted successfully!")


# --- Fonction pour créer l'interface To-Do ---
def create_todo_ui(parent_frame):
    global todo_frame, task_entry, task_list, entryNumber_delete_task

    todo_frame = ctk.CTkFrame(parent_frame, fg_color="transparent")
    todo_frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Chemin de l'image (ajuster si nécessaire)
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_dir, 'image_fx.jpg') # Assurez-vous que l'image existe
        img = ctk.CTkImage(Image.open(img_path), size=(40, 40))
    except FileNotFoundError:
        print("Warning: image_fx.jpg not found. Skipping image.")
        img = None
    except Exception as e:
        print(f"Warning: Could not load image. Error: {e}")
        img = None


    title_label = ctk.CTkLabel(todo_frame,
                               text="My To-Do Task",
                               font=("Comic Sans MS", 28, "italic"),
                               image=img,
                               compound="left")
    title_label.pack(pady=(10, 20))

    task_entry = ctk.CTkEntry(todo_frame,
                              placeholder_text="Enter Your task here!",
                              width=400,
                              height=40,
                              corner_radius=20,
                              font=("Comic Sans MS", 16, "italic"))
    task_entry.pack(pady=(0, 10))

    task_list = ctk.CTkTextbox(todo_frame,
                               width=400,
                               height=200, # Ajuster la hauteur
                               corner_radius=20,
                               font=("Comic Sans MS", 16, "italic"),
                               wrap="none",
                               spacing3=5)
    task_list.pack(pady=(0, 10))

    entryNumber_delete_task = ctk.CTkEntry(todo_frame,
                                           placeholder_text="Enter task number to delete",
                                           width=400,
                                           height=40,
                                           corner_radius=20,
                                           font=("Comic Sans MS", 16, "italic"))
    # Ne pas packer initialement

    button_frame = ctk.CTkFrame(todo_frame, fg_color="transparent")
    button_frame.pack(pady=(5, 10))

    submit_button = ctk.CTkButton(button_frame,
                                  text="Add Task",
                                  font=("Arial", 18),
                                  corner_radius=20,
                                  command=task_submit)
    submit_button.pack(side="left", padx=10)

    delete_button = ctk.CTkButton(button_frame,
                                  text="Delete Task",
                                  font=("Arial", 18),
                                  corner_radius=20,
                                  fg_color="#ff6b6b",
                                  hover_color="#e05252",
                                  command=delete_button_fonction)
    delete_button.pack(side="left", padx=10)


# --- Fonction de connexion (adaptée de login_sys_CTk.py) ---
def attempt_login(username_entry, password_entry, error_label):
    global app # Accéder à la fenêtre principale pour la modifier
    username = username_entry.get()
    password = password_entry.get()

    # Validation simple
    if username == "sepaehs" and password == "123":
        print("Login Successful!")
        # Détruire ou cacher les éléments de connexion
        if login_frame:
            login_frame.pack_forget()
            login_frame.destroy()
        # Créer et afficher l'interface To-Do
        create_todo_ui(app) # Passer la fenêtre principale comme parent
    else:
        print("Login Failed!")
        error_label.configure(text="Wrong username or password!")
        error_label.pack(pady=10) # Afficher le message d'erreur

# --- Fonction pour créer l'interface de connexion ---
def create_login_ui(parent_frame):
    global login_frame

    login_frame = ctk.CTkFrame(parent_frame, fg_color="transparent")
    login_frame.pack(pady=20, padx=20, fill="both", expand=True)

    title_label = ctk.CTkLabel(login_frame,
                               text="Login System",
                               font=("Inter", 32, "bold"))
    title_label.pack(pady=20)

    input_frame = ctk.CTkFrame(login_frame)
    input_frame.pack(pady=20, padx=20)

    username_label = ctk.CTkLabel(input_frame, text="Username", font=("Inter", 20))
    username_label.pack(pady=(0, 5))
    entry_1 = ctk.CTkEntry(input_frame, width=340, height=42, font=("Arial", 20), placeholder_text="Enter username")
    entry_1.pack(pady=10)

    password_label = ctk.CTkLabel(input_frame, text="Password", font=("Inter", 20))
    password_label.pack(pady=(0, 5))
    entry_2 = ctk.CTkEntry(input_frame, width=340, height=42, font=("Arial", 20), placeholder_text="Enter password", show="*")
    entry_2.pack(pady=10)

    error_label = ctk.CTkLabel(login_frame, text="", text_color="red", font=("Inter", 16))
    # Ne pas packer initialement error_label

    login_button = ctk.CTkButton(login_frame,
                                 text="Login",
                                 font=("Inter", 20, "bold"),
                                 width=340,
                                 height=42,
                                 command=lambda: attempt_login(entry_1, entry_2, error_label))
    login_button.pack(pady=20)


# --- Application Principale ---
if __name__ == "__main__":
    ctk.set_appearance_mode("dark") # Ou "light"
    ctk.set_default_color_theme("blue") # Ou une autre couleur

    app = ctk.CTk()
    app.geometry("630x600") # Ajuster la taille si nécessaire
    app.title("Main Application - Login & ToDo")

    # Afficher l'interface de connexion au démarrage
    create_login_ui(app)

    app.mainloop()