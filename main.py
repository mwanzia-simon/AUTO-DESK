
import customtkinter as ctk

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

button = ctk.CTkButton(window,text="Click me!")
button.pack()
window.mainloop()