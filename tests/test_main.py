
import unittest
from io import StringIO
from unittest.mock import patch
import sys
sys.path.insert(0, '../Attess')
from attess.main import run
from attess.main import parseArgs


class TestMain(unittest.TestCase):
    
    def test_parseArgs(self):
        parser = parseArgs(['account', '123123123'])
        assert parser.AccountNumber == 123123123
        assert parser.subparser == 'account'

    def test_run_account(self):
        result = run(['account', '123123123123'])
        assert result == "123123123123"
    
    #https://stackoverflow.com/questions/39028204/using-unittest-to-test-argparse-exit-errors
    @patch('sys.stderr', new_callable=StringIO)
    def test_run_default(self, mock_stderr):
        with self.assertRaises(SystemExit):
            run(['lol'])
        self.assertRegexpMatches(mock_stderr.getvalue(), r"invalid choice")


if __name__ == "__main__":
    unittest.main()