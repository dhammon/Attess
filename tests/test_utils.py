
import unittest
import sys
sys.path.insert(0, '../attess')
from attess.utils import Utils
from io import StringIO
from contextlib import redirect_stdout


class TestUtils(unittest.TestCase):

    def test_displayMessage(self):
        message = "lol"
        f = StringIO()
        with redirect_stdout(f):
            Utils.displayMessage(message, False)
        actual = f.getvalue()
        self.assertIn("lol", actual)
        f.close


if __name__ == "__main__":
    unittest.main()
