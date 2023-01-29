
import unittest
import sys
sys.path.insert(0, '../attess')
import config as cfg
from attess.containers import Containers
from io import StringIO
from contextlib import redirect_stdout
import json
from os import path


class TestContainers(unittest.TestCase):

    def test_bruteforceRepos_happy1(self):
        accountNumber = cfg.testVars["ACCOUNTNUMBER"]  #victim test account
        f = StringIO()
        with redirect_stdout(f):
            Containers.bruteforceRepos(accountNumber)
        actual = f.getvalue()
        self.assertIn("[+]", actual)
        self.assertNotIn("[-]", actual)
        f.close


    def test_bruteforceRepos_happy2(self):
        accountNumber = cfg.testVars["ACCOUNTNUMBER"]  #victim test account
        f = StringIO()
        with redirect_stdout(f):
            Containers.bruteforceRepos(accountNumber, True)
        actual = f.getvalue()
        self.assertIn("[+]", actual)
        self.assertIn("[-]", actual)
        f.close


    def test_bruteforceRepos_happy3_wordlist(self):
        accountNumber = cfg.testVars["ACCOUNTNUMBER"]  #victim test account
        wordlistPath = path.dirname(__file__)+"/data/wordlist.txt"
        f = StringIO()
        with redirect_stdout(f):
            Containers.bruteforceRepos(accountNumber, True, wordlistPath)
        actual = f.getvalue()
        self.assertIn("[+]", actual)
        self.assertIn("[-]", actual)
        self.assertIn("lol", actual)
        f.close


    def test_bruteforceRepos_sad1(self):
        accountNumber = 123123123123
        f = StringIO()
        with redirect_stdout(f):
            Containers.bruteforceRepos(accountNumber)
        actual = f.getvalue()
        self.assertNotIn("[+]", actual)
        self.assertNotIn("[-]", actual)
        f.close


    def test_bruteforceRepos_sad2(self):
        accountNumber = 123123123123
        f = StringIO()
        with redirect_stdout(f):
            Containers.bruteforceRepos(accountNumber, True)
        actual = f.getvalue()
        self.assertNotIn("[+]", actual)
        self.assertIn("[-]", actual)
        f.close
    

    def test_getWordlistLines_happy(self):
        wordlistPath = path.dirname(__file__)+"/../attess/data/ecr.txt"
        lines = Containers.getWordlistLines(wordlistPath)
        result = False
        
        if "public_repo\n" in lines:
            result = True
        
        self.assertTrue(result)


    def test_getWordlistLines_sad(self):
        wordlistPath = path.dirname(__file__)+"/not/exists.txt"
        with self.assertRaises(Exception):
            Containers.getWordlistLines(wordlistPath)


    def test_displayModuleBanner(self):
        accountNumber = "123123123123"
        showFails = False
        wordlistPath = "/some/path"
        f = StringIO()
        with redirect_stdout(f):
            Containers.displayModuleBanner(accountNumber, showFails, wordlistPath)
        actual = f.getvalue()
        self.assertIn("Module: Containers", actual)
        self.assertIn("Account Number: 123123123123", actual)
        self.assertIn("Show Fails: False", actual)
        self.assertIn("Wordlist: /some/path", actual)


    def test_handleResponse_happy1(self):
        response = "[+] some message"
        showFail = False
        f = StringIO()
        with redirect_stdout(f):
            Containers.handleResponse(response, showFail)
        actual = f.getvalue()
        self.assertIn("[+]", actual)
        f.close

    
    def test_handleResponse_happy2(self):
        response = "[+] some message"
        showFail = True
        f = StringIO()
        with redirect_stdout(f):
            Containers.handleResponse(response, showFail)
        actual = f.getvalue()
        self.assertIn("[+]", actual)
        f.close


    def test_handleResponse_sad1(self):
        response = "[-] some message"
        showFail = False
        f = StringIO()
        with redirect_stdout(f):
            Containers.handleResponse(response, showFail)
        actual = f.getvalue()
        self.assertNotIn("[-]", actual)
        f.close


    def test_handleResponse_sad2(self):
        response = "[-] some message"
        showFail = True
        f = StringIO()
        with redirect_stdout(f):
            Containers.handleResponse(response, showFail)
        actual = f.getvalue()
        self.assertIn("[-]", actual)
        f.close


    def test_checkRepo_happy(self):
        accountNumber = cfg.testVars["ACCOUNTNUMBER"]  #victim test account
        repoName = 'public_repo'
        result = Containers.checkRepo(accountNumber, repoName)
        self.assertIn("[+] FOUND Valid ECR Repository!!!", result)


    def test_checkRepo_sad(self):
        accountNumber = "123123123123"
        repoName = 'lol'
        result = Containers.checkRepo(accountNumber, repoName)
        self.assertIn("[-] ECR Repository Invalid", result)


if __name__ == "__main__":
    unittest.main()
