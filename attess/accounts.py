
from attess.account import Account
from sys import stdout
import threading
import time
import math


class Accounts:

    def enumerateAccounts(minNumber: int, maxNumber: int, threads=10, showFails=False):
        Account.validateNumber(minNumber)
        Account.validateNumber(maxNumber)
        Accounts.validateMinLessThanMax(minNumber, maxNumber)
        Accounts.validateThreadCount(threads)
        Accounts.displayModuleBanner(minNumber, maxNumber, threads, showFails)
        Accounts.makeThreads(minNumber, maxNumber, threads, showFails)

        return True
    

    def displayModuleBanner(minNumber, maxNumber, threads, showFails):
        print("Module: Accounts")
        print("Start Account: " + str(minNumber))
        print("End Account: " + str(maxNumber))
        print("Thread Count: " + str(threads))
        print("Show Fails: " + str(showFails))
        print("")
        print("--------------------------------------------------")
        print("")
    
    
    def makeThreads(startNum: int, endNum: int, threads: int, showFails: bool):
        startTime = time.time()
        rangePerThread = math.ceil((endNum - startNum) / threads)
        thread_list = []
        i = 0

        while i < threads:
            first = int(startNum + (rangePerThread*i))
            second = int(startNum + rangePerThread + (rangePerThread*i))
            thread = threading.Thread(target=Accounts.checkAccountNumbers, args=(first,second,i,showFails))
            thread.start()
            thread_list.append(thread)
            i += 1
        
        for thread in thread_list:
            thread.join()

        endTime = time.time()
        seconds = endTime - startTime
        print("Seconds spent: " + str(round(seconds)))
    

    def checkAccountNumbers(startNum: int, endNum: int, iterator: int, showFails: bool):
        for number in range(startNum, endNum):
            response = Account.makeRequest(number)
            Accounts.handleResponse(response, number, showFails)
            Accounts.handlePercentDisplay(iterator, endNum, startNum, number, showFails)


    def handlePercentDisplay(iterator, endNum, startNum, number, showFails):
        if iterator == 0:
            total = endNum - startNum
            numerator = number+1-startNum
            per = round(numerator / total * 100)
            message = "[!] " + str(per) + "% complete"
            if not showFails:
                LINE_UP = '\033[1A'
                LINE_CLEAR = '\x1b[2K'
                print(LINE_UP, end=LINE_CLEAR)    
            print(message)


    def handleResponse(response, number, showFails):
        status = response.status_code
        if status == 302:
            message = "[+] Valid AWS Account Found: " + str(number)
            Accounts.displayMessage(message, showFails)

        if status == 429:
            message = "[!] Status Code 429: Too many requests! Decrease threads!"
            Accounts.displayMessage(message, showFails)
        
        if showFails == True and status != 302 and status != 429:
            message = "[-] Invalid AWS Account: " + str(number)
            Accounts.displayMessage(message, showFails)
    

    def displayMessage(message: str, showFails: bool):
        print(message)
        if not showFails:
            print("")


    def validateMinLessThanMax(minNumber, maxNumber):
        if minNumber >= maxNumber:
            raise TypeError("Min number must be less than max number")


    def validateThreadCount(threads: int):
        if threads <= 0 or threads > 100 or threads % 1 != 0:
            raise TypeError("Threads must be a whole number greater than 0 and less than 101")
