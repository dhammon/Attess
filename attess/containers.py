
import boto3
from os import path
from attess.utils import Utils
from attess.account import Account

class Containers:

    #TODO threaded
    #TODO enumerate valid repo images: aws ecr list-images --registry-id <ACCTNUMBER> --repository-name public_repo
    #TODO specify region


    def bruteforceRepos(accountNumber: str, showFails=False, wordlistPath=path.dirname(__file__)+"/data/ecr.txt"):
        Account.validateNumber(accountNumber)
        Containers.displayModuleBanner(accountNumber, showFails, wordlistPath)
        lines = Containers.getWordlistLines(wordlistPath)

        for repoName in lines:
            message = Containers.checkRepo(accountNumber, repoName.rstrip())
            Containers.handleResponse(message, showFails)
        
        print("[!] Completed")
    

    def getWordlistLines(wordlistPath):
        if not path.isfile(wordlistPath):
            raise Exception("[!] Wordlist file path not found!")
            
        wordlist = open(wordlistPath, 'r')
        lines = wordlist.readlines()
        wordlist.close()

        return lines


    def displayModuleBanner(accountNumber, showFails, wordlistPath):
        print("Module: Containers")
        print("Account Number: " + str(accountNumber))
        print("Show Fails: " + str(showFails))
        print("Wordlist: " + str(wordlistPath))
        print("")
        print("--------------------------------------------------")
        print("")
        

    def handleResponse(response, showFails):
        if "[+]" in response:
            Utils.displayMessage(response, False)
        if showFails == True and "[-]" in response:
            Utils.displayMessage(response, showFails)


    def checkRepo(accountNumber: str, repoName: str):
        client = boto3.client('ecr')
        try:
            client.get_repository_policy(
                registryId=str(accountNumber),
                repositoryName=repoName
            )
            client.close()
            message = "[+] FOUND Valid ECR Repository!!! " + repoName
            return message
        except:
            client.close()
            message = "[-] ECR Repository Invalid " + repoName
            return message
