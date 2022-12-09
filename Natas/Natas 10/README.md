# Natas Level 9 → Level 10

Username: natas9 <br>
URL:      http://natas9.natas.labs.overthewire.org

## SOLUTION

- We log in and once more see a way to interact with the server. We are allowed to do a query, to search for a word in a dictionary. Searching for 'dog', will return multiple words simillar to 'dog'. 

 ![image](https://user-images.githubusercontent.com/44790709/206695876-e14c0ec1-74ba-4d73-ab53-267b64ef4641.png)

- We are also offered a peek at the source code, where we can find something interesting. After looking at the the source code, we see a few things: our input is being saved in a variable named needle and a php script is fetching the contents of 'needle' (which is part of the associative array $\_REQUEST)and save it into a variable, 'key'.
Then, grep is being called on a file, dictionary.txt, with the pattern saved in 'key'. For this, the command *passthru* is being used.

 ![image](https://user-images.githubusercontent.com/44790709/206696045-2266a7d7-f090-4d59-8af5-0bf8ff515bfd.png)

- Using *passthru* like this can lead to a common OWASP vulnerability, code injection. Since any character will go through the query, we can try using bash's command separator, ';', and see if we can inject some code

![image](https://user-images.githubusercontent.com/44790709/206696141-ecf55cb2-6493-4661-9cf3-5b2b7d690f06.png)

- We are able to use ls just as theorized. Lets try printing out the password now

 ![image](https://user-images.githubusercontent.com/44790709/206696286-c6a6728e-6439-474b-b942-b67b1a2dfbf4.png)

- Et voilá
