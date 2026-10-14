
import customtkinter as ctk

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

def button_clicked():
    label.configure(text="AutoDesk is running!")

def greet_user():
    name = name_entry.get()
    label.configure(text=f"Hello, {name}!")
    
label = ctk.CTkLabel(window,text="Welcome to AutoDesk!")
name_entry = ctk.CTkEntry(window,placeholder_text="Enter your name")

button1 = ctk.CTkButton(
    window,
    text="File analyser",
    command=button_clicked
    )

button2 = ctk.CTkButton(
    window,
    text="Bulk Renamer",
    command=button_clicked
    )

button3 = ctk.CTkButton(
    window,
    text="Greet me!",
    command=greet_user
    )

button1.grid(row=0,column=0,pady=10,padx=10)
button2.grid(row=0,column=1,pady=10,padx=10)
button3.grid(row=0,column=2,pady=10,padx=10)
name_entry.grid(row=1,column=0,pady=10,padx=10)
label.grid(row=2,column=0,pady=10,padx=10)


window.mainloop()