

# Natas Level 14 → Level 15

Username: natas14 <br>
URL:      http://natas14.natas.labs.overthewire.org

## SOLUTION

- We log in to see see an input form. We can provide credentials to, apperantly, get the password to the next level. We are also given another sneak peek into the source code. Obviously, when trying to input a random set of credentials we get an "Access denied" warning. 
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/7ba518b8-f263-4340-9008-c0199692fff7)

- A first glance at the source code reveals our next approcah: our input is used as part of a MYSQL query and is very poorly sanitezed. The way the code is written, allows for the user to inject SQL code.
- We can test this by giving **"** as our username. It should give us an error since we will be matching the potential **"** in the code and ending it abruptly
- ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/30d73044-6c8b-4344-8c22-d0e721e3e393)
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/a5b2bff8-af64-4088-98a7-d90b8e92fb35)

- As expected, giving **"** as a username did give unexpected results. We could try to exploit this further. Looking at the code, it seems that to be validated we only our **$query** to return a number of rows larger than 0
- This should be achieved by selecting any register on the users table. We can try to inject SQL code to ahcieve this. 
- We can change our original query:

  SELECT * from users where username=".$_REQUEST["username"]." and password=".$_REQUEST["password"]."

- Into something like:

  SELECT * from users where username=**" or 1=1 #** and password=

- What we're doing is matching the first **"** and allowing anything to be select, since the condition 1=1 will always be true. This will select all users from the table **users** no matter what, thus always returning a number of rows larger than 1 and complying with the condition:
```diff
@@         if(mysqli_num_rows(mysqli_query($link, $query)) > 0)         @@
```
  


- Lets test this:
  
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/f27c5a85-256b-4043-97f0-624c0a2be5b6)


- Et voilá:
  
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/eff4b6ac-1372-4bfd-b96c-fc2d7aeed9de)

