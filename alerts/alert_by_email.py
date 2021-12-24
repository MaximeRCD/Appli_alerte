import smtplib


def send_email(iphone_found):
    gmail_user = 'python.price.advertiser@gmail.com'
    gmail_password = 'Python123'

    sent_from = gmail_user
    to = [gmail_user, 'drichaudeau@equancy.com']

    for iphone in iphone_found:
        subject = "Iphone Found Go Get It !!!"
        body = f"We have found your desired Iphone: \n" \
               f"Let's recap : Your were demanding an Iphone with some specs here is one which satisfies all of them !! \n" \
               f"   - Storage : {iphone[1]}\n" \
               f"   - Color : {iphone[2]}\n" \
               f"   - State : {iphone[3]}\n" \
               f"   - Price <= {iphone[4]}\n" \
               f"   - Check this link: \n" \
               f"               {iphone[5]}\n" \
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

            print('Email sent!')
        except:
            print('Something went wrong...')

    print("Hey, email has been sent!")
