import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.extract import scrape_fashion_data  

class TestExtractData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = scrape_fashion_data()

    def test_scrape_data_not_empty(self):
        self.assertIsNotNone(self.data)
        self.assertGreater(len(self.data), 0, "Data tidak boleh kosong!")

    def test_scrape_data_structure(self):
        sample = self.data[0] if self.data else None  # Cegah error jika data kosong
        self.assertIsNotNone(sample, "Sample data harus tersedia untuk diuji")
        self.assertIsInstance(sample, dict, "Data harus dalam bentuk dictionary")
        for field in ['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender']:
            self.assertIn(field, sample, f"Kolom '{field}' harus ada dalam data")

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)