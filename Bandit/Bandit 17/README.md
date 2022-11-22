# Bandit Level 16 → Level 17
 
## LEVEL GOAL
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000.
First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. 
There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

## SOLUTION

- We start by using nmap once more. Lets use check which services  exist in the port range of interest using -sV on localhost.
 ![image](https://user-images.githubusercontent.com/44790709/203340709-12aa05cf-e3de-435a-9a3b-6b55e9e035da.png)

- We find that port 31790 hosts an unknown ssl service, which can be interesting. Lets give the password to that server and see what happens:
 ![image](https://user-images.githubusercontent.com/44790709/203343073-57cd4a72-ac6c-46d5-9629-c816da8f49b6.png)

- We are in! And aparently, we are given a RSA private key and then we're kicked out. Can we use this to connect to the next level?
 ![image](https://user-images.githubusercontent.com/44790709/203343612-0197399f-95fe-4407-8007-ab39c6686687.png)

- We need to create out .key file. Lets copy the RSA key to a file in our temp folder. We must also change its permissions so that only our user can access it, otherwise it will be ignored.
![image](https://user-images.githubusercontent.com/44790709/203345746-cc079bda-3124-4dfe-915a-517a4a768019.png)
![image](https://user-images.githubusercontent.com/44790709/203345999-2fc57038-a7db-45cf-a177-90995a606f76.png)
![image](https://user-images.githubusercontent.com/44790709/203346211-ebe0cc90-da38-446d-9998-8997a0760d58.png)

- We're in! Lets just get our password for future reference and we're done!
 ![image](https://user-images.githubusercontent.com/44790709/203346956-19483231-aacd-4526-a8c0-894252cb6b2d.png)


- Et voilá  
