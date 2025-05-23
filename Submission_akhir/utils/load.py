import pandas as pd
from utils.transform import transform_data
from utils.extract import scrape_fashion_data

def save_to_csv(dataframe, filename="fashion_data_cleaned.csv"):
    dataframe.to_csv(filename, index=False)
    print(f"Data berhasil disimpan ke {filename} dengan total {len(dataframe)} produk.")

if __name__ == "__main__":

    raw_data = scrape_fashion_data()
    clean_data = transform_data(raw_data)

    save_to_csv(clean_data)