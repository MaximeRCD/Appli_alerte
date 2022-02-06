import smtplib
from IOs.iphone import read_iphone_searched as find_clients


def send_email(user_email,iphone_found):
    """Used to send an email to the person who has precised its  email adress"""

    gmail_user = 'python.price.advertiser@gmail.com'
    gmail_password = 'Python123'

    client_profils = find_clients()
    sent_from = gmail_user


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

                        try:
                            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                            server.ehlo()
                            server.login(gmail_user, gmail_password)
                            server.sendmail(sent_from, to, msg.encode('UTF_8'))
                            server.close()

                            print(f'Email sent to {client["email"]}!')
                        except:
                            print('Something went wrong...')

    print("Hey, email has been sent!")
