
import customtkinter as ctk

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

def button_clicked():
    label.configure(text="AutoDesk is running!")
    
label = ctk.CTkLabel(window,text="Welcome to AutoDesk!")
label.pack()

button = ctk.CTkButton(
    window,
    text="Click me!",
    command=button_clicked
    )
button.pack(padx=30)
window.mainloop()