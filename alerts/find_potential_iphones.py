from IOs.iphone import read_iphone_searched as find_iphones
import time
import pandas as pd
import glob


def search_in_db():

    searched_iphone = find_iphones()
    timestamp = time.strptime(time.strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
    path = f".\\data\\{timestamp.tm_year}\\{timestamp.tm_mon}"##\\{timestamp.tm_mday}"
    #print(searched_iphone)
    #print(path)
    csv_path = glob.glob(f"{path}\\*\\*\\*.csv")
    #print(csv_path)
    # iphone_data = pd.concat([pd.read_csv(csv_file) for csv_file in csv_path ], ignore_index=True)
    # iphone_data.model = list(map(lambda x: str.lower(x).replace(" ", ""), iphone_data['model'].tolist()))
    iphone_found = {}
    for tel in searched_iphone:
        iphone_data = pd.concat([pd.read_csv(csv_file) for csv_file in csv_path], ignore_index=True)
        iphone_data.model = list(map(lambda x: str.lower(x).replace(" ", ""), iphone_data['model'].tolist()))
        iphone_data = iphone_data[iphone_data.model == (str.lower(tel["model"]).replace(" ", ""))]
        iphone_data = iphone_data[iphone_data.stockage == tel["stockage"]]
        iphone_data = iphone_data[iphone_data.prix <= tel["prix"]]
        iphone_data = iphone_data[iphone_data.etat == tel["etat"]]
        iphone_data = iphone_data[iphone_data.couleur == tel["couleur"]]
        try:
            iphone_found[tel["model"]].append(iphone_data.values.tolist())
        except:
            iphone_found[tel["model"]] = []
            iphone_found[tel["model"]].append(iphone_data.values.tolist())
    #print(f"iphone_found = {iphone_found}")

    # drop duplicates because if two people have the same request then each one of them get sent two emails
    deduplicated_list = list()
    for key in iphone_found.keys():
        for item in iphone_found[key]:
            if item not in deduplicated_list:
                deduplicated_list.append(item)
        iphone_found[key]=deduplicated_list
    return iphone_found
