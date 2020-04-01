import tkinter as tk
from tkinter import ttk

def clickme():
    print("You just clicked me")


root=tk.Tk()
click_button=ttk.Button(root,text="click me",command = clickme)
click_button.pack(side="left", fill = "both", expand = True)

quit_button=ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack(side="left",fill="both",expand=True)

root.mainloop()