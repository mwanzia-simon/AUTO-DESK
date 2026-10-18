import customtkinter as ctk
from tkinter import filedialog
from automations.organizer import scan_folder
import os

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

selected_folder = ""

def choose_folder():
    global selected_folder
    file_path = filedialog.askdirectory()
    if file_path:
        selected_folder = file_path
       

def run_organizer():
    print("AutoDesk organizer started!")

    
label = ctk.CTkLabel(window,text="Welcome to AutoDesk!")

button1 = ctk.CTkButton(
    window,
    text="Run Organizer",
    command=run_organizer
    )

button4 = ctk.CTkButton(
    window,
    text="open folder",
    command=choose_folder
    )

button1.grid(row=0,column=0,pady=10,padx=10)
button4.grid(row=0,column=3,pady=10,padx=10)
label.grid(row=2,column=0,pady=10,padx=10)


window.mainloop()