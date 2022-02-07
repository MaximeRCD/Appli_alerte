from IOs.iphone import read_iphone_searched as find_clients
import time
import pandas as pd
import glob
import os


def search_in_db():
    """Used to search the specified iphone by user in the database"""
    client_profils = find_clients()
    current_time = time.strptime(time.strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
    path_to_data = os.path.abspath(f"./data/{current_time.tm_year}/{current_time.tm_mon}")##\\{timestamp.tm_mday}"
    csv_path = glob.glob(os.path.abspath(f"{path_to_data}/*/*/*.csv"))
    iphone_found = {}
    for tel in client_profils:
        iphone_data = pd.concat([pd.read_csv(csv_file) for csv_file in csv_path], ignore_index=True)
        iphone_data.model = list(map(lambda x: str.lower(x).replace(" ", ""), iphone_data['model'].tolist()))
        iphone_data = iphone_data[iphone_data.model == (str.lower(tel["model"]).replace(" ", ""))]
        iphone_data = iphone_data[iphone_data.stockage == tel["stockage"]]
        iphone_data = iphone_data[iphone_data.prix <= tel["prix"]]
        iphone_data = iphone_data[iphone_data.etat == tel["etat"]]
        iphone_data = iphone_data[iphone_data.couleur == tel["couleur"]]
        iphone_data.drop_duplicates()
        try:
            iphone_found[tel["model"]].append(iphone_data.values.tolist())
        except:
            iphone_found[tel["model"]] = []
            iphone_found[tel["model"]].append(iphone_data.values.tolist())

    """drop duplicates because if two people have the same request then each one of them get sent two emails"""
    deduplicated_list = list()
    for key in iphone_found.keys():
        for item in iphone_found[key]:
            if item not in deduplicated_list:
                deduplicated_list.append(item)
        iphone_found[key]=deduplicated_list

    return iphone_found
