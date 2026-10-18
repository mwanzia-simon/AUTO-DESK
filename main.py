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
results_frame.grid_columnconfigure(1,weight=1)
results_frame.grid_columnconfigure(2,weight=1)

selected_folder = ""

def choose_folder():
    global selected_folder
    file_path = filedialog.askdirectory()
    if file_path:
        selected_folder = file_path
        selected_folder_label.configure(text=f"SELECTED FOLDER: {selected_folder}")
       

def run_organizer():
    if selected_folder:
        moved,skipped,failed,success = scan_folder(selected_folder)
        moved_label.configure(text=f"MOVED\n{moved}")
        skipped_label.configure(text=f"SKIPPED\n{skipped}")
        failed_label.configure(text=f"FAILED\n{failed}")
        if not success:
            organization_info_label.configure(text="Could not access the selected folder.")
        elif success and failed == 0:
            organization_info_label.configure(text="Organization complete.")
        else:
            organization_info_label.configure(text="Organization complete with errors.")         
    else:
        organization_info_label.configure(text="Please select a folder!")

results_title = ctk.CTkLabel(
    results_frame,
    text="Organization Results",
    text_color="#F8FAFC",
    anchor="w",
    font=ctk.CTkFont(size=18, weight="bold")
    )
moved_label = ctk.CTkLabel(
    results_frame,
    text="MOVED\n0",
    text_color="#86EFAC",
    fg_color="#123528",
    corner_radius=12,
    font=ctk.CTkFont(size=15, weight="bold"),
    height=76
    )
skipped_label = ctk.CTkLabel(
    results_frame,
    text="SKIPPED\n0",
    text_color="#FCD34D",
    fg_color="#3B2F16",
    corner_radius=12,
    font=ctk.CTkFont(size=15, weight="bold"),
    height=76
    )
failed_label = ctk.CTkLabel(
    results_frame,
    text="FAILED\n0",
    text_color="#FCA5A5",
    fg_color="#3B2025",
    corner_radius=12,
    font=ctk.CTkFont(size=15, weight="bold"),
    height=76
    )

selected_folder_label = ctk.CTkLabel(
    controls_frame,
    text="No folder selected",
    text_color="#94A3B8",
    anchor="w",
    font=ctk.CTkFont(size=13),
    wraplength=650
    )
organization_info_label = ctk.CTkLabel(
    results_frame,
    text="Choose a folder and organize it to see a summary.",
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
results_title.grid(row=0, column=0, columnspan=3, padx=20, pady=(18, 12), sticky="ew")
moved_label.grid(row=1, column=0, padx=(20, 6), pady=(0, 12), sticky="ew")
skipped_label.grid(row=1, column=1, padx=6, pady=(0, 12), sticky="ew")
failed_label.grid(row=1, column=2, padx=(6, 20), pady=(0, 12), sticky="ew")
organization_info_label.grid(row=2, column=0, columnspan=3, padx=20, pady=(4, 18), sticky="nw")


window.mainloop()