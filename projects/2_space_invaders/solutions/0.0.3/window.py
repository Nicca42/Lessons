from tkinter import *
from aliens import alienSetup

window = Tk()
window.title("Space invaiders v0.0.3")
window.geometry('350x200')

alienSetup(window)

player = Label(window, text="P", padx=15, pady=15)
player.grid(column=5, row=1)

window.mainloop()