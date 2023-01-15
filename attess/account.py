

class Account:
    
    def checkAccountNumber(number: int):
        Account.validateNumber(number)
        return number

    def validateNumber(number: int):
        if len(str(number)) != 12:
            raise TypeError("Account number must be 12 digits")