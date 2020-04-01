import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {username.get() or 'World!'}")

root=tk.Tk()

username= tk.StringVar()

name_label=ttk.Label(root, text="NAME")
name_label.pack(side="left", padx=(0,10),fill = "both", expand = True)

name_entry=ttk.Entry(root, width=10, textvariable=username)
name_entry.pack(side="left",fill = "both", expand = True)
name_entry.focus()


greet_button=ttk.Button(root,text="greet",command = greet)
greet_button.pack(side="left", fill = "both", expand = True)

quit_button=ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack(side="left",fill="both",expand=True)

root.mainloop()