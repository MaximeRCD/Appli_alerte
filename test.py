import tkinter as tk

from IOs.iphone import append_new_iphone

if __name__ == '__main__':
    root = tk.Tk()

    def register_window():
        child_w = tk.Toplevel(root)
        child_w.geometry("300x250")
        child_w.grid()
        child_w.title("New Child Window")

        tk.Label(child_w, text="Your email adress :").grid(row=0)
        tk.Label(child_w, text="Iphone model :").grid(row=1)
        tk.Label(child_w, text="Iphone Stockage :").grid(row=2)
        tk.Label(child_w, text="Iphone Renoved State :").grid(row=3)
        tk.Label(child_w, text="Iphone Color :").grid(row=4)
        tk.Label(child_w, text="Maximum Price Desired : ").grid(row=5)

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

        email = tk.Entry(child_w, borderwidth=2)
        iphone_model = tk.OptionMenu(child_w, model_var, *liste_model)
        iphone_stockage = tk.OptionMenu(child_w, stockage_var, *liste_stockage)
        iphone_state = tk.OptionMenu(child_w, state_var, *liste_state)
        iphone_color = tk.OptionMenu(child_w, color_var, *liste_color)
        iphone_price = tk.Entry(child_w, borderwidth=2)

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

            append_new_iphone(user_email, model,stockage, state, color, price)

        tk.Button(child_w, text="Save Profil", command=register_user).grid(column=0, row=6)
        tk.Button(child_w, text="Quit", command=child_w.destroy).grid(column=1, row=6)

    tk.Button(root, text="Register", command=register_window).grid(column=1, row=0)
    # quit button
    tk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()