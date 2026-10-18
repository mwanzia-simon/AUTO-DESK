import customtkinter as ctk
from tkinter import filedialog
from automations.organizer import scan_folder
import os

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

frame = ctk.CTkFrame(window)
frame.pack(expand=True)

selected_folder = ""

def choose_folder():
    global selected_folder
    file_path = filedialog.askdirectory()
    if file_path:
        selected_folder = file_path
        label.configure(text=selected_folder)
       

def run_organizer():
    if selected_folder:
        moved,skipped,failed = scan_folder(selected_folder)
        label2.configure(text=f"Moved:{moved}\n Skipped:{skipped}\n Failed:{failed}")
    else:
        label2.configure(text="Please select a folder!")

    
label = ctk.CTkLabel(frame,text="Welcome to AutoDesk!")
label2 = ctk.CTkLabel(frame,text="File Info.")

button1 = ctk.CTkButton(
    frame,
    text="Run Organizer",
    command=run_organizer
    )

button4 = ctk.CTkButton(
    frame,
    text="open folder",
    command=choose_folder
    )

button1.grid(row=0,column=0,pady=10,padx=10)
button4.grid(row=0,column=3,pady=10,padx=10)
label.grid(row=2,column=0,pady=10,padx=10)
label2.grid(row=3,column=0,pady=10,padx=10)


window.mainloop()