# Natas Level 10 → Level 11

Username: natas10 <br>
URL:      http://natas10.natas.labs.overthewire.org

## SOLUTION

- This time around, we are unable to use some characters. Looking at the source code, it's obvious using ';' won't work this time. However, since the input is not properly sanitized,  we can still exploit grep.
Grep is using the -i flag (case insensitive), using our key as a pattern and looking in 'dictionary.txt'. What happens if we try to use a pattern that has spaces in it?

 ![image](https://user-images.githubusercontent.com/44790709/206700020-16734b12-d555-416d-949a-86e61598ed43.png)
 
- This output is provided when grep is looking for multiple files! Lets emulate this behaviour ion our own shell 

 ![image](https://user-images.githubusercontent.com/44790709/206700243-c3d65c73-95e1-4b62-b204-e42d819e3457.png)

- Grep is now trying to find 'eh' and 'lol.txt' as files to read from! Since there are characters separated by a space, grep reads them as files to look in. This is again exploitable, as we can try matching all characters (.) in our password file

 ![image](https://user-images.githubusercontent.com/44790709/206700449-2d81e7cc-2cdc-4c78-a75a-b2e516a08cb7.png)

- Et voilá
