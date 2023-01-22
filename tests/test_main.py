
import unittest
from io import StringIO
from unittest.mock import patch
import sys
sys.path.insert(0, '../attess')
from contextlib import redirect_stdout
from attess.main import run
from attess.main import parseArgs


class TestMain(unittest.TestCase):
    
    def test_parseArgs_account(self):
        parser = parseArgs(['account', '123123123'])
        assert parser.AccountNumber == 123123123
        assert parser.subparser == 'account'
    

    def test_parseArgs_accounts_default(self):
        parser = parseArgs(['accounts', '123123123123', '123123123123'])
        self.assertEqual(123123123123,parser.EndAccountNumber)
        self.assertEqual(123123123123,parser.StartAccountNumber)
        self.assertEqual(False, parser.show_fails)
        self.assertEqual('accounts', parser.subparser)
        self.assertEqual(10, parser.threads)


    def test_parseArgs_accounts_custom(self):
        parser = parseArgs(['accounts', '123123123123', '123123123123', '--threads=50', '--show-fails'])
        self.assertEqual(123123123123,parser.EndAccountNumber)
        self.assertEqual(123123123123,parser.StartAccountNumber)
        self.assertEqual(True, parser.show_fails)
        self.assertEqual('accounts', parser.subparser)
        self.assertEqual(50, parser.threads)


    def test_run_account(self):
        result = run(['account', '123123123123'])
        self.assertIn("AWS Account", result)
    

    def test_run_accounts_min(self):
        f = StringIO()
        with redirect_stdout(f):
            run(['accounts', '123123123123', '123123123173'])
        actual = f.getvalue()
        self.assertIn("100% complete", actual)
        self.assertIn("Seconds spent", actual)
        f.close


    def test_run_accounts_threads(self):
        f = StringIO()
        with redirect_stdout(f):
            run(['accounts', '123123123123', '123123123173', '--threads=10'])
        actual = f.getvalue()
        self.assertIn("100% complete", actual)
        self.assertIn("Seconds spent", actual)
        f.close


    def test_run_accounts_fails(self):
        f = StringIO()
        with redirect_stdout(f):
            run(['accounts', '123123123123', '123123123173', '--show-fails'])
        actual = f.getvalue()
        self.assertIn("100% complete", actual)
        self.assertIn("Seconds spent", actual)
        self.assertIn("Invalid AWS Account", actual)
        f.close


    #https://stackoverflow.com/questions/39028204/using-unittest-to-test-argparse-exit-errors
    @patch('sys.stderr', new_callable=StringIO)
    def test_run_fail(self, mock_stderr):
        with self.assertRaises(SystemExit):
            run(['lol'])
        self.assertRegexpMatches(mock_stderr.getvalue(), r"invalid choice")


if __name__ == "__main__":
    unittest.main()