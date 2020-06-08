import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from code import datamunger

#Please run this from the terminal with the line: python3 -m unittest test_datamunger.py

class DataMungerTest(unittest.TestCase):
    def test_calc_total(self):
        total = datamunger.calc_total([1708,53,24,13,53,788,323,1,453,6,234]) 
        expected = 53 + 24 + 13 + 53 + 788 + 323 + 1 + 453
        self.assertEqual(total,expected)

    def test_check_row_Correct(self):
        result = datamunger.check_row(1, [0,53,24,13,53,788,323,1,453,6,234], [1708,53,24,13,53,788,323,1,453,6,234])
        expected = True
        self.assertEqual(result,expected)

    def test_check_row_NotMono(self):
        result = datamunger.check_row(1,[0,53,24,13,53,788,323,1,453,6,234], [1706,52,23,13,53,788,323,1,453,6,234])
        self.assertEqual(result,True)

    def test_check_row_Missing(self):
        result = datamunger.check_row(1,[0,53,24,13,53,788,323,1,453,6,234], [' ',52,23,13,53,788,323,1,453,6,234])
        self.assertEqual(result,False)

    def test_check_row_NotTotal(self):
        result = datamunger.check_row(1,[0,53,24,13,53,788,323,1,453,6,234], [1,53,24,13,53,788,323,1,453,6,234])
        self.assertEqual(result,True)

if __name__ == '__main__':
    unittest.main()