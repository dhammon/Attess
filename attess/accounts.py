
from attess.account import Account
import requests
from sys import stdout
import threading
import time
import math


class Accounts:

    def enumerateAccounts(minNumber: int, maxNumber: int, threads=10):
        Account.validateNumber(minNumber)
        Account.validateNumber(maxNumber)
        Accounts.validateMinLessThanMax(minNumber, maxNumber)
        Accounts.validateThreadCount(threads)
        Accounts.makeThreads(minNumber, maxNumber, threads)
    

    #TODO test
    #TODO breakup
    def makeThreads(startNum: int, endNum: int, threads: int):
        startTime = time.time()
        rangePerThread = math.ceil((endNum - startNum) / threads)
        thread_list = []
        i = 0

        while i < threads:
            first = int(startNum + (rangePerThread*i))
            second = int(startNum + rangePerThread + (rangePerThread*i))
            thread = threading.Thread(target=Accounts.checkAccountNumbers, args=(first,second,i))
            thread.start()
            thread_list.append(thread)
            i += 1
        
        for thread in thread_list:
            thread.join()

        endTime = time.time()
        seconds = endTime - startTime
        print("Seconds spent: " + str(round(seconds)))
    

    def checkAccountNumbers(startNum: int, endNum: int, iterator: int):
        for number in range(startNum, endNum):
            response = Account.makeRequest(number)
            Accounts.handleResponse(response, number)
            Accounts.handlePercentDisplay(iterator, endNum, startNum, number)


    def handlePercentDisplay(iterator, endNum, startNum, number):
        if iterator == 0:
            total = endNum - startNum
            numerator = number+1-startNum
            per = round(numerator / total * 100)
            LINE_UP = '\033[1A'
            LINE_CLEAR = '\x1b[2K'
            print(LINE_UP, end=LINE_CLEAR)
            print(str(per) + "% complete")


    def handleResponse(response, number):
        if response.status_code == 302:
            message = "[+] Valid AWS Account Found: " + str(number)
            LINE_UP = '\033[1A'
            LINE_CLEAR = '\x1b[2K'
            print(LINE_UP, end=LINE_CLEAR)
            print(message)
            print("")

        if response.status_code == 429:
            message = "[!] Status Code 429: Too many requests! Decrease threads!"
            print(message)


    def validateMinLessThanMax(minNumber, maxNumber):
        if minNumber >= maxNumber:
            raise TypeError("Min number must be less than max number")


    def validateThreadCount(threads: int):
        if threads <= 0 or threads > 100 or threads % 1 != 0:
            raise TypeError("Threads must be a whole number greater than 0 and less than 101")
