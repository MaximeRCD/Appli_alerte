import json


def read_iphone_searched():
    """
    From the searched_iphone file
    :return: a list of iphone
    """
    with open("searched_iphone.json", encoding='UTF_8') as file_of_searched_iphones:
        return json.loads(file_of_searched_iphones.read())


def append_new_iphone(email, model, stockage, etat, couleur, prix):
    iphone_searched = {"email": email,
                       "model": model,
                       "stockage": int(stockage),
                       "etat": etat,
                       "couleur": couleur,
                       "prix": int(prix)}

    iphone_tableau = read_iphone_searched()
    iphone_tableau.append(iphone_searched)
    print(iphone_tableau)

    with open(".\\searched_iphone.json", mode='w', encoding='UTF_8') as f:
        f.write(json.dumps(iphone_tableau, ensure_ascii=False))

