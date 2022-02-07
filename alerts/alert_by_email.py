import smtplib, ssl
from tkinter import messagebox

from IOs.iphone import read_iphone_searched as find_clients


def send_email(user_email,iphone_found):
    """Used to send an email to the person who has precised its  email adress"""

    gmail_user = 'pythopriceadvertiser@gmail.com'
    gmail_application_password = 'nwhylcpchkymjvta'

    client_profils = find_clients()
    sent_from = gmail_user
    number_of_sent_email = 0
    for client in client_profils:
        if user_email == client["email"]:
            to = [client["email"]]
            for all_tel in iphone_found[client["model"]]:
                for tel in all_tel:
                    if tel[0] == client['model'].lower().replace(" ","") and tel[1] == client["stockage"] and tel[2] == client["couleur"] and tel[3] == client["etat"] and tel[4] <= client["prix"]:
                        subject = "Iphone Found Go Get It !!!"
                        body = f"We have found your desired Iphone: \n" \
                               f"Let's recap : Your were demanding an Iphone with some specs here is one which satisfies all of them !! \n" \
                               f"   - name : {tel[0]}\n" \
                               f"   - Storage : {tel[1]}\n" \
                               f"   - Color : {tel[2]}\n" \
                               f"   - State : {tel[3]}\n" \
                               f"   - Price : {tel[4]}\n" \
                               f"   - Check this link: \n" \
                               f"               {tel[5]}\n" \
                               f"We thank you for your confidence.\n" \
                               f"Don't hesitate to recommend us around you.\n\n\n" \
                               f"Have a good day.\n" \
                               f"Baye and Maxime."

                        msg = f"Subject:{subject}\n\n{body}"
                        print(tel)
                        number_of_sent_email += 1
                        try:
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls(context=ssl.create_default_context())
                            server.login(gmail_user, gmail_application_password)
                            server.ehlo()
                            server.sendmail(sent_from, to, msg.encode('UTF_8'))
                            server.quit()
                            messagebox.showinfo("Great News", f"An email has been sent to {client['email']} !")
                        except Exception as e:
                            messagebox.showerror("Very Bad News", f"The following error occured {e}. Please contact us at :"
                                                                  f"pythopriceadvertiser@gmail.com")
            if number_of_sent_email == 0:
                messagebox.showinfo("Bad News", f"Sorry, We did not find your desired Iphone ! "
                                                f"Try to launch another Scrap or come back later.")
