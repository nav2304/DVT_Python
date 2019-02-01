import tkinter as tk
from tkinter import *
#Add Frame  To window

dvt = tk.Tk()
dvt.title("Data Validation Tool")
dvt.geometry("900x300")
source1Frame = Frame(dvt)
v = IntVar()
print(v)
Radiobutton(dvt, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(dvt, text='MIT', variable=v, value=2).pack(anchor=W)


source1Frame.pack()
dvt.resizable(height=False, width=False)
label: Label = tk.Label(dvt, width=20)
label.pack(side="top", fill="both", expand=True, padx=20, pady=20)

def handle_configure(event):
    text="window geometry:\n" + dvt.geometry()
    label.configure(text=text)

dvt.bind("<Configure>", handle_configure)

dvt.mainloop()