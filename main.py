
import customtkinter as ctk

window = ctk.CTk()

window.title("AutoDesk | Automation Center")
window.geometry("800x500")

def button_clicked():
    print("The button was clicked!")

button = ctk.CTkButton(
    window,
    text="Click me!",
    command=button_clicked
    )
button.pack()
window.mainloop()