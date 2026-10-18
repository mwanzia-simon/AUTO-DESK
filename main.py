import customtkinter as ctk
from tkinter import filedialog
from automations.organizer import scan_folder
import os

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

# frame = ctk.CTkFrame(window)
# frame.pack(expand=True)

controls_frame = ctk.CTkFrame(
    window,
    corner_radius=12,
    fg_color="#1E293B"
    )
results_frame = ctk.CTkFrame(window)

controls_frame.pack(padx=20,pady=10,fill="x")
results_frame.pack(padx=20,pady=10,fill="x")

controls_frame.grid_columnconfigure(0,weight=1)
controls_frame.grid_columnconfigure(1,weight=1)

results_frame.grid_columnconfigure(0,weight=1)

selected_folder = ""

def choose_folder():
    global selected_folder
    file_path = filedialog.askdirectory()
    if file_path:
        selected_folder = file_path
        selected_folder_label.configure(text=f"SELECTED FOLDER: {selected_folder}")
       

def run_organizer():
    if selected_folder:
        moved,skipped,failed = scan_folder(selected_folder)
        organization_info_label.configure(text=f"Moved:{moved}\n\n Skipped:{skipped}\n\n Failed:{failed}")
    else:
        organization_info_label.configure(text="Please select a folder!")

    
selected_folder_label = ctk.CTkLabel(controls_frame,text="")
organization_info_label = ctk.CTkLabel(results_frame,text="File Info.")
app_name =ctk.CTkLabel(controls_frame,text="AutoDesk - File Organizer")
select_folder_text = ctk.CTkLabel(controls_frame,text="Select the folder you want to organize.")

run_organizer_btn = ctk.CTkButton(
    controls_frame,
    text="Run Organizer",
    command=run_organizer
    )

open_folder_btn = ctk.CTkButton(
    controls_frame,
    text="Browse",
    command=choose_folder
    )

# controls_frame
app_name.grid(row=0,column=0,pady=10,padx=10)
open_folder_btn.grid(row=1,column=1,pady=10,padx=10)
select_folder_text.grid(row=1,column=0,pady=10,padx=10)
run_organizer_btn.grid(row=3,column=1,pady=10,padx=10)

selected_folder_label.grid(
    row=2,
    column=0,
    pady=10,
    padx=10,
    columnspan=2,
    sticky="ew"
    )

#  results_frame 
organization_info_label.grid(
    row=0,
    column=0,
    pady=10,
    padx=10,
    sticky="ew"
    )


window.mainloop()