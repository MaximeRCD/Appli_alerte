import time
import _io
import os


def open_init_data_file(type_iphone):
    """
    :return: file in which we wite scrapped data
    """
    timestamp = time.strptime(time.strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
    path = os.path.abspath(f"./data/{timestamp.tm_year}/{timestamp.tm_mon}/{timestamp.tm_mday}/{timestamp.tm_hour}")

    if not os.path.exists(path):
        os.makedirs(path)

    f = open(os.path.abspath(f"{path}/{type_iphone}_{time.strftime('%H-%M-%S')}.csv"), 'w', encoding='UTF-8')
    f.write(f"model,stockage,couleur,etat,prix,lien\n")
    return f


def fill_file(file, name, capacite, couleur, state, price, lien):
    if name != None:
        file.write(f"{name},{capacite},{couleur},{state},{price},{lien}\n")


def close_file(file: _io.TextIOWrapper):
    """
    :type file: TextIO
    """
    file.close()