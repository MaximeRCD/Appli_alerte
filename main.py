from IOs.data import open_init_data_file, fill_file, close_file
from IOs.urls import read_urls
from alerts.alert_by_email import send_email
from alerts.find_potential_iphones import search_in_db
from scrap.scrapping import get_all_iphone_div, get_iphone_all_details


if __name__ == '__main__':

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
    send_email(search_in_db())






