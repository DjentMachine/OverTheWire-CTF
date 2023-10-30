# Natas Level 15 → Level 16

Username: natas15 <br>
URL:      http://natas15.natas.labs.overthewire.org


## SOLUTION

- Once more we see an input form. We can now submit some text to see whether it exists as a user in the table. To check its behaviour, we try "natas16" as a user, since I assume that would be the user for the next level.
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/2cbb5e3d-2bfb-4024-8a2b-91be8fc71280)
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/b0c641f0-016a-4376-aa46-3698cf28b758)


- Checking the source code one thing immidiatly stands out: there is a commented "CREATE TABLE" statement at the beggining of the script. I assume there is a table "users" which was creted with this statement and someone lefted it here commented for little reason. I'll assume our username and password both are strings (varchar) with maximum 64 characters in length.
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/37e84438-0d76-4f50-a375-5d8410435456)


- Reading on, we see a simillar piece of code to the previous exercice. Only this time, instead of granting access after meeting a condition, this script simply tells us if a user exists in the users table.

- Once more, the input is poorly sanitized which allows us to inject SQL code. However, we'll need to be inventive here. Since we already know the username of interest, "natas16", we can try to fetch its password from the users table. But there seems to be no obvious way to print its contents.  
 
- I see 2 potential ways to exploit this. Either we do reconaissanse on the target to see whether we can spawn a shell through our input or we can try to bruteforce our binary response into telling us which characters comprise the password. We'll use the second approach:
  
- The server responds with either a "user exists" (1) or with a user doesn't exist (0). Knowing this, the username and a bit of regex we should be able to bruteforce our way through the password. We can try matching the user **"natas16"** and anything starting with an **"a"**. If indeed our password starts with an **a**, the server should respond with a 1. Otherwise, it responds with 0. We can iterate through all the relevant unicode characters to see which one starts our password. Our test input should be as follows:
```diff
@@                natas16" AND password like "a%"               @@
``` 
- The result is:
  
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/a1507654-606c-4e47-8f6f-18b56f38c262)

-  Alas, our password does not start with **"a"**. Let's try this for other characters
  
