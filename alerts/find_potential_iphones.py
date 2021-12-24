from IOs.iphone import read_json as find_iphones
import time
import pandas as pd
import glob


def search_in_db():

    searched_iphone = find_iphones()
    timestamp = time.strptime(time.strftime("%Y/%m/%d %H:%M:%S"), "%Y/%m/%d %H:%M:%S")
    path = f"C:\\Users\\maxim\\PYTHON\\Appli_alerte\\data\\{timestamp.tm_year}\\{timestamp.tm_mon}\\{timestamp.tm_mday}\\11"
    print(searched_iphone)

    iphone_data = pd.concat([pd.read_csv(csv_file) for csv_file in glob.glob(f"{path}\\*.csv")], ignore_index=True)
    iphone_data.model = list(map(lambda x: str.lower(x).replace(" ", ""), iphone_data['model'].tolist()))

    for tel in searched_iphone:
        iphone_data = iphone_data[iphone_data.model == (str.lower(tel["model"]).replace(" ", ""))]
        iphone_data = iphone_data[iphone_data.stockage == tel["stockage"]]
        iphone_data = iphone_data[iphone_data.prix <= tel["prix"]]
        iphone_data = iphone_data[iphone_data.etat == tel["etat"]]
        iphone_data = iphone_data[iphone_data.couleur.isin(tel["couleur"])]
        print(iphone_data.values.tolist())
        return iphone_data.values.tolist()