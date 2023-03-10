
import requests


class Account:
    
    def checkAccountNumber(number: int):
        Account.validateNumber(number)
        Account.displayModuleBanner(number)
        response = Account.makeRequest(number)
        message = Account.handleResponse(response, number)
        
        return message
    

    def displayModuleBanner(number):
        print("Module: Account")
        print("Account Number: " + str(number))
        print("")
        print("--------------------------------------------------")
        print("")
    

    def handleResponse(response, number):
        if response.status_code == 302:
            message = "[+] Valid AWS Account Found: " + str(number)

            return message
            
        else:
            message = "[-] Invalid AWS Account: " + str(number)

            return message
    

    def makeRequest(number: int):
        url = "https://"+str(number)+".signin.aws.amazon.com/console"
        response = requests.get(url, allow_redirects=False)

        return response


    def validateNumber(number: int):
        if len(str(number)) != 12 or number % 1 != 0:
            raise TypeError("Account number must be 12 whole digits")