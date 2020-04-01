import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {username.get() or 'World!'}")

root=tk.Tk()

input_frame1=ttk.Frame(root,padding=(10,20,20,0))
input_frame1.pack(fill="both")
input_frame2=ttk.Frame(root,padding=(10,20))
input_frame2.pack(fill="both")


username= tk.StringVar()

name_label=ttk.Label(input_frame1, text="NAME")
name_label.pack(side="left", padx=(0,10))

name_entry=ttk.Entry(input_frame1, width=10, textvariable=username)
name_entry.pack(side="left",fill = "x", expand = True)
name_entry.focus()



greet_button=ttk.Button(input_frame2,text="greet",command = greet)
greet_button.pack(side="left", fill = "x", expand = True)

quit_button=ttk.Button(input_frame2,text="Quit",command=root.destroy)
quit_button.pack(side="left",fill="x",expand=True)

root.mainloop()