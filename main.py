import smtplib
import schedule
import time
from IOs.data import open_init_data_file, fill_file, close_file
from IOs.urls import read_urls
from scrap.scrapping import get_all_iphone_div, get_iphone_all_details


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('python.price.advertiser@gmail.com', 'Python123')

    subject = "Price fell down"
    body = "Check this link: https://www.amazon.in/Apple-iPhone-11-64GB-Green/dp/B07XVKBY68/ref=sr_1_7?keywords=iphone+11&qid=1573668357&sr=8-7"
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail("Sender's email", "Recipientemail", msg)

    print("Hey, email has been sent!")
    server.quit()


if __name__ == '__main__':

    def main_action():
        all_urls = read_urls()
        print(all_urls)
        for url in all_urls:
            iPhones_divs, type_iphone = get_all_iphone_div(url)
            print(type_iphone)
            file = open_init_data_file(type_iphone)
            for iphone in iPhones_divs:
                name, capacity, color, state, price = get_iphone_all_details(iphone)
                print(name, capacity, color, state, price)
                fill_file(file, name, capacity, color, state, price)
            close_file(file)


    schedule.every(2).hours.do(main_action())
    while True:
        schedule.run_pending()
        time.sleep(1)


