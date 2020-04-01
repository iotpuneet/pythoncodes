import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {username.get() or 'You did not enter anything'}")

root=tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)

input_frame1=ttk.Frame(root,padding=(10,20,20,0))
input_frame1.grid(row=0, column=0)
input_frame2=ttk.Frame(root,padding=(10,20))
input_frame2.grid(sticky="EW")


username= tk.StringVar()

name_label=ttk.Label(input_frame1, text="NAME")
name_label.grid(row=0, column=0,padx=(0,10))

name_entry=ttk.Entry(input_frame1, width=15, textvariable=username)
name_entry.grid(row=0, column=1)
name_entry.focus()

input_frame2.columnconfigure(0, weight=1)
input_frame2.columnconfigure(1, weight=1)

greet_button=ttk.Button(input_frame2,text="greet",command = greet)
greet_button.grid(row=0, column=0, sticky="EW")

quit_button=ttk.Button(input_frame2,text="Quit",command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")


root.mainloop()