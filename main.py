import customtkinter as ctk
from tkinter import filedialog
from automations.organizer import scan_folder
import os

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

def choose_folder():
    file_path = filedialog.askdirectory()
    items = os.listdir(file_path)
    print(items)
    label.configure(text=file_path)

def run_organizer():
    print("AutoDesk organizer started!")

    
label = ctk.CTkLabel(window,text="Welcome to AutoDesk!")

button1 = ctk.CTkButton(
    window,
    text="File analyser",
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