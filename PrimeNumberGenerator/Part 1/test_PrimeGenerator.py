import unittest
from PrimeGenerator import GetPrime1,GetPrime2

class TestPrimeNum(unittest.TestCase):
    def test_prime(self):
        if GetPrime1:
            self.assertTrue(GetPrime1)
        if GetPrime2:
            self.assertTrue(GetPrime2)
if __name__ == '__main__':
    unittest.main()