# Bandit Level 15 → Level 16
 
## LEVEL GOAL
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

## SOLUTION

- Since we're asked to connect using ssl/tsl encryption, we can use openssl to do so. Lets use local host and port 30001. We might as well use the s_clients' -ign_eof flag as suggested.
 ![image](https://user-images.githubusercontent.com/44790709/203338940-f9ff65ba-4785-489f-b811-37ab36b2041c.png)

- We're asked for a prompt after the 'Read R BLOCK' message. Lets give it the password                
 ![image](https://user-images.githubusercontent.com/44790709/203341441-34e854aa-50a2-42b1-9354-3e0f63f0f501.png)
 
- Et voilá

 
