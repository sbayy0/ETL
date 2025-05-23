import pandas as pd
from utils.extract import scrape_fashion_data

def clean_price(price):
    if isinstance(price, str) and "$" in price:
        try:
            return float(price.replace("$", "").strip()) * 16000
        except ValueError:
            return None
    return None

def clean_rating(rating):
    if isinstance(rating, str):
        rating = rating.replace("Rating: ⭐", "").replace("Rating:", "").replace("/ 5", "").strip()
        try:
            return float(rating)
        except ValueError:
            return None
    return None

def clean_colors(colors):
    if isinstance(colors, str):
        colors = colors.replace(" Colors", "").strip()
        return int(colors) if colors.isdigit() else None
    return None

def extract_size(text):
    if isinstance(text, str) and "Size:" in text:
        return text.split("Size:")[-1].strip()
    return text if isinstance(text, str) else None

def extract_gender(text):
    if isinstance(text, str) and "Gender:" in text:
        return text.split("Gender:")[-1].strip()
    return text if isinstance(text, str) else None

def transform_data(raw_data):

    df = pd.DataFrame(raw_data)

    print("\n**Data SEBELUM transformasi:**")
    print(df.head())

    df['Price'] = df['Price'].apply(clean_price)
    df['Rating'] = df['Rating'].apply(clean_rating)
    df['Colors'] = df['Colors'].apply(clean_colors)
    df['Size'] = df['Size'].apply(extract_size)
    df['Gender'] = df['Gender'].apply(extract_gender)

    print("\n**Data SETELAH transformasi:**")
    print(df.head())

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    print("\n**Cek jumlah data kosong per kolom:**")
    print(df.isnull().sum())
    print("\n**Jumlah data duplikat:**", df.duplicated().sum())

    return df

if __name__ == "__main__":
    raw_data = scrape_fashion_data() 
    transformed_data = transform_data(raw_data)  