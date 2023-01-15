
import unittest
import sys
sys.path.insert(0, '../Attess')
from attess.account import Account


class TestAccount(unittest.TestCase):
    
    def test_checkAccountNumber_happy(self):
        result = Account.checkAccountNumber(123456789012)
        assert result == 123456789012

    def test_checkAccountNumber_sad(self):
        with self.assertRaises(TypeError):
            Account.checkAccountNumber(123)

    def test_validateNumber_happy(self):
        result = Account.validateNumber(123456789012)
        self.assertIsNone(result)
    
    def test_validateNumber_sad(self):
        with self.assertRaises(TypeError):
            Account.validateNumber(123)


if __name__ == "__main__":
    unittest.main()