
import argparse
from attess.account import Account
from attess.accounts import Accounts


def parseArgs(inputs):

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser")

    #account
    account_parser = subparsers.add_parser('account', help='Check AWS account number validity')
    account_parser.add_argument('AccountNumber', type=int, action='store', help='12 digit AWS account number')
    
    #accounts
    accounts_parser = subparsers.add_parser('accounts', help='Check a range of AWS account numbers for validity')
    accounts_parser.add_argument('StartAccountNumber', type=int, action='store', help='Starting 12 digit AWS account number')
    accounts_parser.add_argument('EndAccountNumber', type=int, action='store', help='Ending 12 digit AWS account number')
    accounts_parser.add_argument('--threads', type=int, action='store', default=10, help='Threads; more is faster but will run into AWS rate limits.  Default=10')
    accounts_parser.add_argument('--show-fails', action='store_true', default=False, help='Show failed attempts.  Default=False')

    args = parser.parse_args(inputs)

    return args


def run(inputs):

    args = parseArgs(inputs)

    if args.subparser == 'account':
        result = Account.checkAccountNumber(args.AccountNumber)

        return result
    
    if args.subparser == 'accounts':
        result = Accounts.enumerateAccounts(args.StartAccountNumber, args.EndAccountNumber, args.threads, args.show_fails)

        return result
    
    parseArgs(["--help"])
