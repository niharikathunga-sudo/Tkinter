"""import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("light")   # "light" or "dark"
ctk.set_default_color_theme("green")  # "blue", "green", "dark-blue"

# Create main window
top = ctk.CTk()
top.title("Login Me")
top.geometry("450x300")
top.configure(fg_color="pink")  # background color

# Username label and entry
user_label = ctk.CTkLabel(top, text="Username", text_color="black", fg_color="pink")
user_label.place(x=40, y=60)
user_name_entry = ctk.CTkEntry(top, width=200, fg_color="white", text_color="black")
user_name_entry.place(x=110, y=60)

# Password label and entry
pass_label = ctk.CTkLabel(top, text="Password", text_color="black", fg_color="pink")
pass_label.place(x=40, y=100)

user_password_entry = ctk.CTkEntry(top, width=200, show="*", fg_color="white", text_color="black")
user_password_entry.place(x=110, y=100)
# Toggle password visibility
def toggle_password():
    if show_var.get() == 1:
        user_password_entry.configure(show="")
    else:
        user_password_entry.configure(show="*")

show_var = ctk.IntVar()
show_check = ctk.CTkCheckBox(top, text="Show Password", variable=show_var,
command=toggle_password, fg_color="pink",
                             text_color="black", hover_color="lightblue")
show_check.place(x=110, y=125)

# Submit button
submit_btn = ctk.CTkButton(top, text="Submit", fg_color="purple", hover_color="violet",
                           text_color="white", command=top.destroy)
submit_btn.place(x=110, y=160)
top.mainloop()"""


import tkinter as tk
from tkinter import ttk

# Create main window
top = tk.Tk()
top.title("Login Me")
top.geometry("450x300")
top.configure(bg="pink")  # background color

# Define styles
style = ttk.Style()
style.theme_use("default")

# Label style
style.configure("TLabel", background="pink", foreground="blue")

# Entry style
style.configure("TEntry", fieldbackground="lightyellow", foreground="black")

# Button style
style.configure("TButton", background="purple", foreground="white")
style.map("TButton",
          background=[("active", "violet")],
          foreground=[("active", "yellow")])

# Checkbutton style
style.configure("TCheckbutton", background="pink", foreground="darkgreen")
style.map("TCheckbutton",
          background=[("active", "lightblue")],
          foreground=[("active", "red")])

# Username label and entry
ttk.Label(top, text="Username").place(x=40, y=60)
user_name_entry = ttk.Entry(top, width=30)
user_name_entry.place(x=110, y=60)

# Password label and entry
ttk.Label(top, text="Password").place(x=40, y=100)
user_password_entry = ttk.Entry(top, width=30, show="*")
user_password_entry.place(x=110, y=100)

# Toggle password visibility
def toggle_password():
    user_password_entry.config(show="" if show_var.get() else "*")

show_var = tk.BooleanVar()
ttk.Checkbutton(top, text="Show Password", variable=show_var,
                command=toggle_password).place(x=110, y=125)

# Submit button
ttk.Button(top, text="Submit", command=top.destroy).place(x=110, y=160)

top.mainloop()