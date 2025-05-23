import requests
from bs4 import BeautifulSoup

BASE_URL = "https://fashion-studio.dicoding.dev"

def get_page_url(page):
    if page == 1:
        return BASE_URL 
    return f"{BASE_URL}/page{page}"

def scrape_page(page):
    url = get_page_url(page)
    response = requests.get(url)
    print(f"Halaman {page}: Status Code {response.status_code}")

    if response.status_code != 200:
        print(f"Gagal mengambil data dari halaman {page}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    product_list = soup.find_all("div", class_="collection-card")

    if not product_list:
        print(f"Halaman {page}: Tidak ada produk ditemukan")
        return []

    print(f"Halaman {page}: {len(product_list)} produk ditemukan")  
    products = []

    for item in product_list:
        title_element = item.find("h3", class_="product-title")
        price_element = item.find("span", class_="price")
        rating_element = item.find("p", string=lambda text: text and "Rating" in text)
        colors_element = item.find("p", string=lambda text: text and "Colors" in text)
        size_element = item.find("p", string=lambda text: text and "Size" in text)
        gender_element = item.find("p", string=lambda text: text and "Gender" in text)

        products.append({
            "Title": title_element.get_text(strip=True) if title_element else "Unknown Title",
            "Price": price_element.get_text(strip=True) if price_element else "Price Unavailable",
            "Rating": rating_element.get_text(strip=True) if rating_element else "Invalid Rating",
            "Colors": colors_element.get_text(strip=True) if colors_element else "0 Colors",
            "Size": size_element.get_text(strip=True) if size_element else "Unknown Size",
            "Gender": gender_element.get_text(strip=True) if gender_element else "Unknown Gender"
        })

    return products

def scrape_fashion_data():
    all_products = []
    for page in range(1, 51):
        all_products.extend(scrape_page(page))
    return all_products
