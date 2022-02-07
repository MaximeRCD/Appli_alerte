import tkinter as tk
from tkinter import messagebox

from IOs.iphone import append_new_iphone
from IOs.data import open_init_data_file, fill_file, close_file
from IOs.urls import read_urls
from alerts.alert_by_email import send_email
from alerts.find_potential_iphones import search_in_db
from scrap.scrapping import get_all_iphone_div, get_iphone_all_details
from utils.utility import test_email, test_price, email_in_db


def scrapping_window(root):
    child_scrapping = tk.Toplevel(root)
    child_scrapping.geometry("300x250")
    child_scrapping.title("Scrapping Window")
    text = tk.Text(child_scrapping)
    text.insert(tk.INSERT, "This part is used to scrap BackMarket\n"
                           "The process is an hour long.\n\n"
                           "If you want to update the database\n"
                           "Please click on Send a Scrap\n\n"
                           "Else Quit to go back to main menu.")
    # disabled text modifications in this window
    text["state"] = "disabled"
    text.insert(tk.END, "")
    text.pack()
    def scrapping_function():
        all_urls = read_urls()
        print(all_urls)
        for url in all_urls:
            iPhones_divs, type_iphone = get_all_iphone_div(url)
            print(type_iphone)
            file = open_init_data_file(type_iphone)
            for iphone in iPhones_divs:
                all_stat = get_iphone_all_details(iphone)
                print(all_stat)
                for stat in all_stat:
                    try:
                        fill_file(file, stat[0], stat[1], stat[2], stat[3], stat[4], stat[5])
                    except TypeError:
                        pass
            close_file(file)
        messagebox.showinfo("Great News", f"The Scrapping is finished !")
    # Button to send email
    tk.Button(child_scrapping, text="Send a scrap on BackMarket", command=scrapping_function).place(x=0, y=220)
    # quit button
    tk.Button(child_scrapping, text="Quit", command=child_scrapping.destroy).place(x=250, y=220)


def email_window(root):
    child_email = tk.Toplevel(root)
    child_email.geometry("300x250")
    child_email.title("Email Window")

    text = tk.Text(child_email)
    text.insert(tk.INSERT, "This part is used to send email\n"
                           "to user who has already registered.\n\n"
                           "If you want to be advise by email if\n"
                           "we have found the corresponding one.\n"
                           "Please fill the text box with the \n"
                           "email you chose at registration\n"
                           "and click on Send an Email.\n\n"
                           "Else Quit to go back to main menu."
                )
    # disabled text modifications in this window
    text["state"] = "disabled"
    text.insert(tk.END, "")
    text.pack()

    tk.Label(child_email, text="Your email adress :").place(x=0, y=180)
    email = tk.Entry(child_email, borderwidth=2)
    email.place(x=150, y=180)

    def email_sender():
        user_email = email.get()
        if email_in_db(user_email):
            if test_email(user_email):
                send_email(user_email, search_in_db())
            else:
                messagebox.showerror("Error", "Your email address is not valid, please enter the right one")
        else:
            messagebox.showerror("Error", "You are not register yet or you misspell your email please retry or register !")

    # Button to send email
    tk.Button(child_email, text="Send an email", command=email_sender).place(x=0, y=220)
    # quit button
    tk.Button(child_email, text="Quit", command=child_email.destroy).place(x=250, y=220)


def register_window(root):
    child_register = tk.Toplevel(root)
    child_register.geometry("300x300")
    child_register.grid()
    child_register.title("Registration Window")

    text = tk.Text(child_register)
    text.insert(tk.INSERT, "This part is used to register\n"
                           "all details we need to find your\n"
                           "desired Iphone and send the alert\n"
                           "by email!\n\n"
                )
    # disabled text modifications in this window
    text["state"] = "disabled"
    text.insert(tk.END, "")
    text.pack()

    tk.Label(child_register, text="Your email adress :").place(x=0, y=80)
    tk.Label(child_register, text="Iphone model :").place(x=0, y=110)
    tk.Label(child_register, text="Iphone Stockage :").place(x=0, y=140)
    tk.Label(child_register, text="Iphone Renoved State :").place(x=0, y=170)
    tk.Label(child_register, text="Iphone Color :").place(x=0, y=200)
    tk.Label(child_register, text="Maximum Price Desired(€):").place(x=0, y=230)

    liste_model = ["iPhone 12", "iPhone 12 mini", "iPhone 12 Pro", "iPhone 12 Pro Max", "iPhone 11",
                   "iPhone 11 Pro", "iPhone 11 Pro Max"]
    liste_stockage = [16, 32, 64, 128, 256, 512]
    liste_state = ["État correct", "Très bon état", "Parfait état", "Comme neuf"]
    liste_color = ["Noir", "(PRODUCT)Red", "Rouge", "Bleu", "Bleu pacifique", "Or", "Jaune", "Argent", "Vert nuit",
                   "Vert", "Gris sidéral", "Blanc", "Mauve"]

    model_var = tk.StringVar()
    stockage_var = tk.IntVar()
    state_var = tk.StringVar()
    color_var = tk.StringVar()

    model_var.set("iPhone 12")
    stockage_var.set(64)
    state_var.set("État correct")
    color_var.set("Noir")

    email = tk.Entry(child_register, borderwidth=2)
    iphone_model = tk.OptionMenu(child_register, model_var, *liste_model)
    iphone_stockage = tk.OptionMenu(child_register, stockage_var, *liste_stockage)
    iphone_state = tk.OptionMenu(child_register, state_var, *liste_state)
    iphone_color = tk.OptionMenu(child_register, color_var, *liste_color)
    iphone_price = tk.Entry(child_register, borderwidth=2)

    email.place(x=150, y=80)
    iphone_model.place(x=165, y=110)
    iphone_stockage.place(x=185, y=140)
    iphone_state.place(x=165, y=170)
    iphone_color.place(x=185, y=200)
    iphone_price.place(x=150, y=230)

    def register_user():
        user_email = email.get()
        price = iphone_price.get()
        color = color_var.get()
        state = state_var.get()
        stockage = stockage_var.get()
        model = model_var.get()
        if test_email(user_email):
            if test_price(price):
                append_new_iphone(user_email, model, stockage, state, color, price)
                messagebox.showinfo("Great News", f"You have well registered yourself !")
            else:
                messagebox.showerror("Error", "The price must be between 100 and 99 999 € and a positive integer")
        else:
            messagebox.showerror("Error", "Your email address is not valid")
    tk.Button(child_register, text="Save Profil", command=register_user).place(x=0, y=260)
    tk.Button(child_register, text="Quit", command=child_register.destroy).place(x=250, y=260)