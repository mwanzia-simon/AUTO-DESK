import customtkinter as ctk
from tkinter import filedialog
from automations.organizer import scan_folder
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x540")
window.minsize(560, 420)
window.configure(fg_color="#0B1120")

# frame = ctk.CTkFrame(window)
# frame.pack(expand=True)

controls_frame = ctk.CTkFrame(
    window,
    corner_radius=16,
    fg_color="#111C2F",
    border_width=1,
    border_color="#24334A"
    )
results_frame = ctk.CTkFrame(
    window,
    corner_radius=16,
    fg_color="#111C2F",
    border_width=1,
    border_color="#24334A"
    )

controls_frame.pack(padx=24, pady=(24, 12), fill="x")
results_frame.pack(padx=24, pady=(0, 24), fill="both", expand=True)

controls_frame.grid_columnconfigure(0,weight=1)
controls_frame.grid_columnconfigure(1,weight=0)

results_frame.grid_columnconfigure(0,weight=1)
results_frame.grid_rowconfigure(0,weight=1)

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

    
selected_folder_label = ctk.CTkLabel(
    controls_frame,
    text="No folder selected",
    text_color="#94A3B8",
    anchor="w",
    font=ctk.CTkFont(size=13)
    )
organization_info_label = ctk.CTkLabel(
    results_frame,
    text="Your organization summary will appear here.",
    text_color="#CBD5E1",
    anchor="nw",
    justify="left",
    font=ctk.CTkFont(size=14),
    padx=20,
    pady=20
    )
app_name = ctk.CTkLabel(
    controls_frame,
    text="AutoDesk  /  File Organizer",
    text_color="#F8FAFC",
    anchor="w",
    font=ctk.CTkFont(size=23, weight="bold")
    )
select_folder_text = ctk.CTkLabel(
    controls_frame,
    text="Choose a folder to organize",
    text_color="#CBD5E1",
    anchor="w",
    font=ctk.CTkFont(size=14)
    )

run_organizer_btn = ctk.CTkButton(
    controls_frame,
    text="Organize files",
    command=run_organizer,
    height=42,
    corner_radius=10,
    font=ctk.CTkFont(size=14, weight="bold")
    )

open_folder_btn = ctk.CTkButton(
    controls_frame,
    text="Browse",
    command=choose_folder,
    height=38,
    width=110,
    corner_radius=9,
    fg_color="#243B5A",
    hover_color="#315277",
    font=ctk.CTkFont(size=13, weight="bold")
    )

# controls_frame
app_name.grid(row=0, column=0, columnspan=2, pady=(20, 8), padx=22, sticky="ew")
select_folder_text.grid(row=1, column=0, pady=(8, 12), padx=22, sticky="ew")
open_folder_btn.grid(row=1, column=1, pady=(8, 12), padx=(10, 22))

selected_folder_label.grid(
    row=2,
    column=0,
    pady=(0, 14),
    padx=22,
    columnspan=2,
    sticky="ew"
    )
run_organizer_btn.grid(row=3, column=0, columnspan=2, pady=(0, 20), padx=22, sticky="ew")

#  results_frame 
organization_info_label.grid(
    row=0,
    column=0,
    pady=0,
    padx=0,
    sticky="nsew"
    )


window.mainloop()