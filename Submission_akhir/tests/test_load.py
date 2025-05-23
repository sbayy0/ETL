import sys
import os
import unittest
import pandas as pd
from utils.load import load_data  

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
class TestLoadData(unittest.TestCase):

    def setUp(self):
        
        self.df = pd.DataFrame([
            {'Title': 'T-shirt', 'Price': 1600000, 'Rating': 4.5, 'Colors': 5, 'Size': 'M', 'Gender': 'Men'},
            {'Title': 'Hoodie', 'Price': 3208000, 'Rating': 3.9, 'Colors': 3, 'Size': 'L', 'Gender': 'Women'}
        ])
        self.test_file = "fashion_data_cleaned.csv"

    def test_save_to_csv(self):
        
        load_data(self.df)  
        loaded_df = pd.read_csv(self.test_file)

        self.assertEqual(len(loaded_df), len(self.df))

        self.assertListEqual(list(loaded_df.columns), list(self.df.columns))

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)




