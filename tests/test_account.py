
import unittest
import sys
sys.path.insert(0, '../attess')
import config as cfg
from attess.account import Account
from io import StringIO
from contextlib import redirect_stdout


class TestAccount(unittest.TestCase):
    
    def test_checkAccountNumber_happy(self):
        f = StringIO()
        with redirect_stdout(f):
            result = Account.checkAccountNumber(123456789012)
        assert result == "[-] Invalid AWS Account: 123456789012"
        f.close()


    def test_checkAccountNumber_sad(self):
        with self.assertRaises(TypeError):
            Account.checkAccountNumber(123)


    def test_displayModuleBanner(self):
        f = StringIO()
        with redirect_stdout(f):
            Account.displayModuleBanner(123123123123)
        self.assertIn("Module: Account", f.getvalue())
        self.assertIn("Account Number: 123123123123", f.getvalue())
        f.close()


    def test_handleResponse_happy(self):
        number = 123123123123
        class Response:
            status_code = 302
        response = Response()
        result = Account.handleResponse(response, number)
        assert result == "[+] Valid AWS Account Found: 123123123123"


    def test_handleResponse_sad(self):
        number = 123123123123
        class Response:
            status_code = 404
        response = Response()
        result = Account.handleResponse(response, number)
        assert result == "[-] Invalid AWS Account: 123123123123"


    def test_makeRequest_happy(self):
        result = Account.makeRequest(cfg.testVars["ACCOUNTNUMBER"])
        assert result.status_code == 302


    def test_makeRequest_sad(self):
        result = Account.makeRequest(123123123123)
        assert result.status_code == 404


    def test_validateNumber_happy(self):
        result = Account.validateNumber(cfg.testVars["ACCOUNTNUMBER"])
        self.assertIsNone(result)


    def test_validateNumber_sad(self):
        with self.assertRaises(TypeError):
            Account.validateNumber(123)


    def test_validateNumber_sad(self):
        with self.assertRaises(TypeError):
            Account.validateNumber(123.123123123)


if __name__ == "__main__":
    unittest.main()