import encodings
import json


def read_json():
    """
    From the searched_iphone file
    :return: a list of iphone
    """
    with open("C:\\Users\\maxim\\PYTHON\\Appli_alerte\\searched_iphone.json", encoding='UTF_8') as file_of_searched_iphones:
        return json.loads(file_of_searched_iphones.read())
