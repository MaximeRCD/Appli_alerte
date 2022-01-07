import tkinter as tk
from functools import partial

from Tkinter.all_windows import scrapping_window, email_window, register_window

if __name__ == '__main__':
    root = tk.Tk()
    # Button to update data
    tk.Button(root, text="Mise a jour des données", command=partial(scrapping_window, root)).grid(column=3, row=0)
    # Button to send email
    tk.Button(root, text="Send an email", command=partial(email_window, root)).grid(column=3, row=1)
    # Button to register a new request
    tk.Button(root, text="Register", command=partial(register_window, root)).grid(column=1, row=1)
    # quit button
    tk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=2)
    root.mainloop()






