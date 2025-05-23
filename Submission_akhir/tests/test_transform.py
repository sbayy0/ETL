import sys
import os
import unittest
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.transform import transform_data

class TestTransformData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Mengambil contoh data hanya sekali sebelum semua test dijalankan."""
        cls.sample_data = [
            {'Price': '$100.00', 'Rating': 'Rating: ⭐ 4.5 / 5', 'Colors': '5 Colors', 'Size': 'Size: M', 'Gender': 'Gender: Men'},
            {'Price': '$200.50', 'Rating': 'Rating: ⭐ 3.9 / 5', 'Colors': '3 Colors', 'Size': 'Size: L', 'Gender': 'Gender: Women'}
        ]
        cls.df = transform_data(cls.sample_data)

    def test_transformed_data_not_empty(self):
        """Pastikan data setelah transformasi tidak kosong."""
        self.assertGreater(len(self.df), 0, "Data hasil transformasi tidak boleh kosong!")

    def test_price_transformation(self):
        """Pastikan harga dikonversi ke Rupiah dengan benar."""
        expected_prices = [100.00 * 16000, 200.50 * 16000]
        self.assertListEqual(self.df['Price'].tolist(), expected_prices)

    def test_rating_extraction(self):
        """Pastikan rating dikonversi ke float dengan benar."""
        expected_ratings = [4.5, 3.9]
        self.assertListEqual(self.df['Rating'].tolist(), expected_ratings)

    def test_colors_extraction(self):
        """Pastikan jumlah warna dikonversi ke angka saja."""
        expected_colors = [5, 3]
        self.assertListEqual(self.df['Colors'].tolist(), expected_colors)

    def test_size_extraction(self):
        """Pastikan ukuran sudah bersih tanpa label 'Size:'."""
        expected_sizes = ['M', 'L']
        self.assertListEqual(self.df['Size'].tolist(), expected_sizes)

    def test_gender_extraction(self):
        """Pastikan gender sudah bersih tanpa label 'Gender:'."""
        expected_genders = ['Men', 'Women']
        self.assertListEqual(self.df['Gender'].tolist(), expected_genders)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)