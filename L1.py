from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(background="blue")
btn = Button(
    root,
    text="Click Me",
    bg="cyan",
    fg="black"
)

btn.pack(side="left")

root.mainloop()