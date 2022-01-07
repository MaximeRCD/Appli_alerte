import tkinter as tk
from IOs.iphone import append_new_iphone
from IOs.data import open_init_data_file, fill_file, close_file
from IOs.urls import read_urls
from alerts.alert_by_email import send_email
from alerts.find_potential_iphones import search_in_db
from scrap.scrapping import get_all_iphone_div, get_iphone_all_details


def scrapping_window(root):
    child_scrapping = tk.Toplevel(root)
    child_scrapping.geometry("300x250")
    child_scrapping.grid()
    child_scrapping.title("Scrapping Window")
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
    # Button to send email
    tk.Button(child_scrapping, text="Send a scrap on BackMarket", command=scrapping_function).grid(column=2, row=1)
    # quit button
    tk.Button(child_scrapping, text="Quit", command=child_scrapping.destroy).grid(column=1, row=2)


def email_window(root):
    child_email = tk.Toplevel(root)
    child_email.geometry("300x250")
    child_email.grid()
    child_email.title("Email Window")
    tk.Label(child_email, text="Your email adress :").grid(row=0)
    email = tk.Entry(child_email, borderwidth=2)
    email.grid(row=0, column=1)

    def email_sender():
        user_email = email.get()
        send_email(user_email, search_in_db())

    # Button to send email
    tk.Button(child_email, text="Send an email", command=email_sender).grid(column=2, row=2)
    # quit button
    tk.Button(child_email, text="Quit", command=child_email.destroy).grid(column=1, row=2)


def register_window(root):
    child_register = tk.Toplevel(root)
    child_register.geometry("300x250")
    child_register.grid()
    child_register.title("New Child Window")

    tk.Label(child_register, text="Your email adress :").grid(row=0)
    tk.Label(child_register, text="Iphone model :").grid(row=1)
    tk.Label(child_register, text="Iphone Stockage :").grid(row=2)
    tk.Label(child_register, text="Iphone Renoved State :").grid(row=3)
    tk.Label(child_register, text="Iphone Color :").grid(row=4)
    tk.Label(child_register, text="Maximum Price Desired : ").grid(row=5)

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

    email.grid(row=0, column=1)
    iphone_model.grid(row=1, column=1)
    iphone_stockage.grid(row=2, column=1)
    iphone_state.grid(row=3, column=1)
    iphone_color.grid(row=4, column=1)
    iphone_price.grid(row=5, column=1)

    def register_user():
        user_email = email.get()
        price = iphone_price.get()
        color = color_var.get()
        state = state_var.get()
        stockage = stockage_var.get()
        model = model_var.get()

        append_new_iphone(user_email, model, stockage, state, color, price)

    tk.Button(child_register, text="Save Profil", command=register_user).grid(column=0, row=6)
    tk.Button(child_register, text="Quit", command=child_register.destroy).grid(column=1, row=6)