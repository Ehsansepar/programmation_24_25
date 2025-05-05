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
