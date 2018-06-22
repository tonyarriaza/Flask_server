import os
import json
import requests
from pprint import pprint
from medical_dictionary import medical_dictionary

class parse_OCR():
    def __init__(self):
        self.DICTIONARY = medical_dictionary()
        self.BOOLEAN = False
        self.OCR_RESULT = ""
        self.listofItems = []
#Dictionary needs to be replaced with a proper dictionary class
#it should iterate over all the medication names looking for a match. Once a result is found it should return a string with the result
    def parse(self,OCR_RESULT):
        LOWERCASE_OCR_STRING= OCR_RESULT.lower()
        toReturn= OCR_RESULT
        self.OCR_RESULT= OCR_RESULT
        utf_string = self.DICTIONARY.CHECK_DICTIONARY(OCR_RESULT)
        byte_string = utf_string.encode('utf8')
        dict_result=str(byte_string)
        utf_OCR_RESULT =OCR_RESULT.lower()
        byte_string = utf_string.encode('utf8')
        LOWERCASE_OCR_STRING=str(byte_string)
        if  dict_result in LOWERCASE_OCR_STRING:
            self.BOOLEAN = True
            self.listofItems.append(dict_result)
            self.listofItems.append(self.BOOLEAN)
            self.listofItems.append(self.OCR_RESULT)
            return self.listofItems
            
            

            
            
            

    