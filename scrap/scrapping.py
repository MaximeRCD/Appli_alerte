import urllib.request
from bs4 import BeautifulSoup
from time import sleep


def get_all_iphone_div(url):
    """
    From the urls in the url file, get the div which contains all product references
    :param url:
    :return: the div with all iphone references
    """
    reponse = urllib.request.urlopen(url)
    documents_bien_parse = BeautifulSoup(reponse.read(), 'html.parser')
    grosse_div = documents_bien_parse('div', {'class': '_22EzdAoZfEubZZ9CBuovRl'})
    all_iphones = grosse_div[0].find_all('a', {})
    type_iphone = grosse_div[0]\
        .find_all('h2', {"class":"font-body text-3 leading-3 font-bold _2xkoCemRpVvAyafHpgIPdC"})[0].contents[0]\
        .strip().replace(" ","_")
    return all_iphones, type_iphone


def get_iphone_all_details(iphone):
    """
    From the page of a particular Iphone, scrap data such as name,
    capacity, color, current state and price and return them.

    """
    all_statistique=[]
    sleep(10)
    racine = 'https://www.backmarket.fr'
    lien = racine + iphone.get('href')
    page_iphone = BeautifulSoup(urllib.request.urlopen(lien).read(), 'html.parser')

    info = page_iphone.find_all('div', {'class': "flex flex-col lg:max-w-[38rem]"})
    info = info[0].find_all('h1', {
        'class': "font-title-latin font-black leading-5 text-7 md:leading-9 md:text-8 _2Z_ijnAN !text-[2.2rem] md:!text-[2.8rem]"})
    name = info[0].contents[0].string.strip()

    if name.startswith('i'):
        """ Don't want to get other device than iPhones. """
        capacity, color = (
            info[0].contents[1].contents[0].string.strip().split('-')[0].replace(" Go", "").strip(),
            info[0].contents[1].contents[0].string.strip().split('-')[1].strip())

        all_states = page_iphone.find_all('ul', {'class': "loHSHcZZByZr-x4WqY6HB grid grid-cols-3 gap-2"})[
            0].find_all('li')

        for current_state in all_states:
            try:
                state, price = (current_state.contents[0]
                                .find_all('p')[0].contents[0]
                                .string.strip()), \
                               (current_state.contents[0]
                                    .find_all('p')[1].contents[0]
                                    .string.strip()
                                    .replace("\u202f","")
                                    .replace(",", ".")[:-2])
                all_statistique.append([name, capacity, color, state, price, lien])
            except AttributeError:
                """ Catch errors due to finding mention like 'déjà vendu' instead of a price """
                pass
        return all_statistique
    else:
        return None, None, None, None, None
