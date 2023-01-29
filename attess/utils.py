
from os import environ
import boto3

class Utils:
    
    def displayMessage(message: str, showFails: bool):
        print(message)
        if not showFails:
            print("")
