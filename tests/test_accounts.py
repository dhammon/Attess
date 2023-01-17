
import unittest
import sys
sys.path.insert(0, '../attess')
from attess.accounts import Accounts
from io import StringIO
from contextlib import redirect_stdout


class TestAccounts(unittest.TestCase):

    def test_enumerateAccounts_happy(self):
        f = StringIO()
        with redirect_stdout(f):
            Accounts.enumerateAccounts(134672723820, 134672723850)
        self.assertIn("Valid AWS Account Found", f.getvalue())
        self.assertNotIn("Status Code 429", f.getvalue())
        f.close()
    
    
    def test_checkAccountNumbers_happy(self):
        f = StringIO()
        with redirect_stdout(f):
            Accounts.checkAccountNumbers(134672723820, 134672723850, 1)
        self.assertIn("Valid AWS Account Found", f.getvalue())
        self.assertNotIn("Status Code 429", f.getvalue())
        f.close()


    def test_handlePercentDisplay_0(self):
        f = StringIO()
        with redirect_stdout(f):
            Accounts.handlePercentDisplay(0, 200, 100, 150)
        actual = f.getvalue()
        self.assertIn("51% complete", actual)
        f.close()


    def test_handleResponse_302(self):
        f = StringIO()
        class Response:
            status_code = 302
        response = Response()
        with redirect_stdout(f):
            Accounts.handleResponse(response, 123123123123)
        self.assertIn("Valid AWS Account Found", f.getvalue())
        f.close()


    def test_handleResponse_429(self):
        f = StringIO()
        class Response:
            status_code = 429
        response = Response()
        with redirect_stdout(f):
            Accounts.handleResponse(response, 123123123123)
        self.assertIn("Status Code 429", f.getvalue())
        f.close()


    def test_validateMinLessThanMax_happy(self):
        result = Accounts.validateMinLessThanMax(1,2)
        self.assertIsNone(result)


    def test_validateMinLessThanMax_sad(self):
        with self.assertRaises(TypeError):
            Accounts.validateMinLessThanMax(2,1)


    def test_validateThreadCount_happy(self):
        result = Accounts.validateThreadCount(50)
        self.assertIsNone(result)


    def test_validateThreadCount_sad1(self):
        with self.assertRaises(TypeError):
            Accounts.validateThreadCount(123)


    def test_validateThreadCount_sad2(self):
        with self.assertRaises(TypeError):
            Accounts.validateThreadCount(-1000)


    def test_validateThreadCount_sad3(self):
        with self.assertRaises(TypeError):
            Accounts.validateThreadCount("abc")


    def test_validateThreadCount_sad4(self):
        with self.assertRaises(TypeError):
            Accounts.validateThreadCount("10")


    def test_validateThreadCount_sad5(self):
        with self.assertRaises(TypeError):
            Accounts.validateThreadCount(10.5)


if __name__ == "__main__":
    unittest.main()
