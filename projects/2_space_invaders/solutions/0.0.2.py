from tkinter import *

window = Tk()
window.title("Space invaiders v0.0.2")
window.geometry('350x200')

alien1 = Label(window, text="A", padx=15, pady=15)
alien1.grid(column=0, row=0)

alien2 = Label(window, text="A", padx=15, pady=15)
alien2.grid(column=1, row=0)

alien3 = Label(window, text="A", padx=15, pady=15)
alien3.grid(column=2, row=0)

alien4 = Label(window, text="A", padx=15, pady=15)
alien4.grid(column=3, row=0)

alien5 = Label(window, text="A", padx=15, pady=15)
alien5.grid(column=4, row=0)

player = Label(window, text="P", padx=15, pady=15)
player.grid(column=5, row=1)

window.mainloop()