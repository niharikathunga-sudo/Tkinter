from tkinter import * 
from tkinter.ttk import *

window=Tk()
window.title("MENUUU")

#creating the menu bar
menubar=Menu(window)

# creatng the file menu & its commands
file=Menu(menubar)
menubar.add_cascade(label="FILE",menu=file)
file.add_command(label="NEW FILE",command=None)
file.add_command(label="NEW WINDOW",command=None)
file.add_command(label="NEW FOLDER",command=None)
file.add_separator()
file.add_command(label="EXIT",command=None)

#creating the edit menu & its commands
edit=Menu(menubar)
menubar.add_cascade(label="EDIT",menu=edit)
edit.add_command(label="UNDO",command=None)
edit.add_command(label="REDO",command=None)
edit.add_command(label="CUT",command=None)
edit.add_command(label="COPY",command=None)
edit.add_command(label="PASTE",command=None)
edit.add_separator()
edit.add_command(label="EXIT",command=None)

window.config(menu=menubar)

#progressbar
progress=Progressbar(window,orient=HORIZONTAL,length=100,mode="determinate")
def stock():
    import time
    progress["value"]=20
    window.update_idletasks()
    window.after(1000)


    progress["value"]=40
    window.update_idletasks()
    window.after(1000)

    progress["value"]=60
    window.update_idletasks()
    window.after(1000)

    progress["value"]=80
    window.update_idletasks()
    window.after(1000)

    progress["value"]=100

progress.pack(pady=100)

btn=Button(window,text="Click here to start!!!",command=stock)
btn.pack(pady=20)







mainloop()

