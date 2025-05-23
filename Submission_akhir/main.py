import sys
import os
import logging

# Tambahkan path ke folder `utils/` agar modul bisa dikenali
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "utils")))

from utils.extract import scrape_fashion_data
from utils.transform import transform_data
from utils.load import load_data

# Konfigurasi logging untuk pemantauan proses
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        # Extract
        logging.info("Mulai mengambil data...")
        raw_data = scrape_fashion_data()

        if not raw_data:
            logging.error("Data yang diambil kosong! Proses dihentikan.")
            return

        # Transform
        logging.info("Mulai melakukan transformasi data...")
        transformed_data = transform_data(raw_data)

        if transformed_data.empty:
            logging.error("Data hasil transformasi kosong! Proses dihentikan.")
            return

        # Load
        logging.info("Mulai menyimpan data...")
        load_data(transformed_data)

        logging.info("ETL pipeline berhasil dijalankan!")

    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()