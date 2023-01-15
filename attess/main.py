
import argparse
from attess.account import Account

def parseArgs(inputs):
    #https://gist.github.com/mdelotavo/07a5337426201685f8d2cb1f5c061d61
    #https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser")

    parser_one = subparsers.add_parser('account', help='Check AWS account number validity')
    parser_one.add_argument('AccountNumber', type=int, action='store', help='12 digit AWS account number')
    
    #parser_two = subparsers.add_parser('two', help='parser two')
    #subparser_two = parser_two.add_subparsers()
    #subparser_two_comment = subparser_two.add_parser('comment-two')
    #subparser_two_comment.add_argument('opt-two', action='store', help='option two')

    args = parser.parse_args(inputs)

    return args


def run(inputs):
    args = parseArgs(inputs)

    if args.subparser == 'account':
        number = Account.checkAccountNumber(args.AccountNumber)
        return str(number)
    
    parseArgs(["--help"])