#!/usr/bin/env python3
import threading
import requests
import time
import math
import sys

def checkNumber(startNum, endNum, iterator):
	for number in range(startNum, endNum):
		url = "https://"+str(number)+".signin.aws.amazon.com/console"
		response = requests.get(url, allow_redirects=False)
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
		if iterator == 0:
			total = endNum - startNum
			numerator = number+1-startNum
			per = round(numerator / total * 100)
			LINE_UP = '\033[1A'
			LINE_CLEAR = '\x1b[2K'
			print(LINE_UP, end=LINE_CLEAR)
			print(str(per) + "% complete")
			#sys.stdout.write(str(per) + "% complete")
			#sys.stdout.write("\r")


if __name__ =="__main__":
	startTime = time.time()

	startNum = 134672722600
	endNum =   134672723900
	threads = 10  #max of 10 otherwise we get 429s
	rangePerThread = math.ceil((endNum - startNum) / threads)

	thread_list = []
	i = 0

	while i < threads:
		first = int(startNum + (rangePerThread*i))
		second = int(startNum + rangePerThread + (rangePerThread*i))
		thread = threading.Thread(target=checkNumber, args=(first,second,i))
		thread.start()
		thread_list.append(thread)
		i += 1
	
	for thread in thread_list:
		thread.join()

	endTime = time.time()
	seconds = endTime - startTime
	print("Seconds spent: " + str(round(seconds)))
