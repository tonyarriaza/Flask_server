import re
import os
import json
import requests
from pprint import pprint


class medical_dictionary():
    def __init__(self):
        self.QUERY=""
        self.BOOLEAN=False
        self.MATCH=""
        self.DICTIONARY=[]
    def CHECK_DICTIONARY(self,OCR_QUERY):
        try:
            with open('/home/ec2-user/environment/Flask_server/result.json') as data_file:  
                data = json.load(data_file)
                # iterates through the list of Dictionaries gets back the name of the medication turns it into a string 
                # lowercases the string then checks if the string is in the Query
                for DICTIONARY in data:
                    utf_string = DICTIONARY.get('name').lower()
                    byte_string = utf_string.encode('utf8')
                    CHECK_NAME=str(byte_string)
                    FINAL_COMPARISON=str(re.sub(r'\(.*\)', '',CHECK_NAME))
                    #print FINAL_COMPARISON
                    utf_string_QUERY= OCR_QUERY.lower()
                    byte_string_QUERY =utf_string.encode('utf8')
                    
                    QUERY_TO_STRING=str(byte_string_QUERY)
                    if FINAL_COMPARISON in QUERY_TO_STRING:
                        return FINAL_COMPARISON
        except Exception as e: 
            print(e)
#x= medical_dictionary()
#x.CHECK_DICTIONARY("buspirone")