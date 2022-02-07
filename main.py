import tkinter as tk
from functools import partial

from Tkinter.all_windows import scrapping_window, email_window, register_window

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x250")
    text = tk.Text(root)
    text.insert(tk.INSERT, "This application is useful to be\n"
                           "alerted by email if we find an\n"
                           "Iphone which you would like to buy.\n\n"
                           "To register your profil please click\n"
                           "Register. If you already have an\n"
                           "account please click send email.\n\n"
                           "Else quit or update DB (1h aprox)")
    #disabled text modifications in this window
    text["state"] = "disabled"
    text.insert(tk.END, "")
    text.pack()
    # Button to update data
    tk.Button(root, text="Update database", command=partial(scrapping_window, root)).place(x=0, y=220)
    # Button to send email
    tk.Button(root, text="Send an email",  command=partial(email_window, root)).place(x=0, y=190)
    # Button to register a new request
    tk.Button(root, text="Register", command=partial(register_window, root)).place(x=0, y=160)
    # quit button
    tk.Button(root, text="Quit", command=root.destroy).place(x=250, y=220)
    root.mainloop()






