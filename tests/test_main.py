
import unittest
from io import StringIO
from unittest.mock import patch
import sys
sys.path.insert(0, '../attess')
from contextlib import redirect_stdout
from attess.main import run
from attess.main import parseArgs


class TestMain(unittest.TestCase):

    def test_parseArgs_surface(self):
        parser = parseArgs(['surface', 'us-east-1'])
        assert parser.Region == 'us-east-1'
        assert parser.subparser == 'surface'        


    def test_run_surface(self):
        f = StringIO()
        with redirect_stdout(f):
            result = run(['surface', 'us-east-1'])
        actual = f.getvalue()
        self.assertIn("[", actual)
        self.assertIn("]", actual)
        f.close
    

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
    

    def test_parseArgs_containers_default(self):
        parser = parseArgs(['containers', '123123123123'])
        self.assertEqual(123123123123,parser.AccountNumber)
        self.assertEqual(False,parser.show_fails)
        self.assertIn("data/ecr.txt", parser.wordlist)
        self.assertEqual('containers', parser.subparser)


    def test_parseArgs_containers_custom(self):
        parser = parseArgs(['containers', '123123123123', '--show-fails', '--wordlist=/tmp/lol.txt'])
        self.assertEqual(123123123123,parser.AccountNumber)
        self.assertEqual(True,parser.show_fails)
        self.assertIn("/tmp/lol.txt", parser.wordlist)
        self.assertEqual('containers', parser.subparser)


    def test_run_account(self):
        f = StringIO()
        with redirect_stdout(f):
            result = run(['account', '123123123123'])
        actual = f.getvalue()
        self.assertIn("AWS Account", result)
        f.close
    

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
    

    def test_run_containers_default(self):
        f = StringIO()
        with redirect_stdout(f):
            run(['containers', '123123123123'])
        actual = f.getvalue()
        self.assertIn("[!] Completed", actual)
        f.close


    def test_run_containers_showFails(self):
        f = StringIO()
        with redirect_stdout(f):
            run(['containers', '123123123123', "--show-fails"])
        actual = f.getvalue()
        self.assertIn("[-] ECR Repository Invalid", actual)
        self.assertIn("[!] Completed", actual)
        f.close


    #https://stackoverflow.com/questions/39028204/using-unittest-to-test-argparse-exit-errors
    @patch('sys.stderr', new_callable=StringIO)
    def test_run_fail(self, mock_stderr):
        with self.assertRaises(SystemExit):
            run(['[lol]'])
        self.assertRegexpMatches(mock_stderr.getvalue(), r"invalid choice")


if __name__ == "__main__":
    unittest.main()