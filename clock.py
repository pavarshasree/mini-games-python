from tkinter import *
from datetime import datetime

root = Tk()
root.title("Varsha's Digital Clock")
root.geometry("500x300")
root.config(bg="#1e1e2f")

def update_time():
    now = datetime.now()
    time_string = now.strftime("%I:%M:%S %p")
    date_string = now.strftime("%A, %d %B %Y")

    time_label.config(text=time_string)
    date_label.config(text=date_string)

    root.after(1000, update_time)

title_label = Label(root, text="Digital Clock",
                    font=("Helvetica", 20, "bold"),
                    bg="#1e1e2f",
                    fg="#ff4da6")
title_label.pack(pady=10)

time_label = Label(root,
                   font=("Helvetica", 50, "bold"),
                   bg="#1e1e2f",
                   fg="#00ffff")
time_label.pack()

date_label = Label(root,
                   font=("Helvetica", 18),
                   bg="#1e1e2f",
                   fg="white")
date_label.pack(pady=10)

footer_label = Label(root,
                     text="Project by Varsha 💙",
                     font=("Arial", 12),
                     bg="#1e1e2f",
                     fg="#ffcc00")
footer_label.pack(side="bottom", pady=10)

update_time()
root.mainloop()
