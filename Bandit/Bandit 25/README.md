# Bandit Level 24 → Level 25
 
## LEVEL GOAL
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode.
There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

## SOLUTION

- Ah, a classic bruteforce challange. An easy one, nonetheless. We already know the size of our pin code, which makes things quite easier. We first experiment with our daemon using netcat to get a feel of how it works
 ![image](https://user-images.githubusercontent.com/44790709/203612113-021ec1d1-0be7-4aab-bd86-8f50d3ef5cde.png)

- We should be able to break this with a simple shellscript. Lets create one that echoes the password and a pincode into netcat. The only trouble is that the daemon doesn't end our session and immidiatly asks for further imput. Our first try can be manually forcing termination using timeout                                              
 ![image](https://user-images.githubusercontent.com/44790709/203611937-9333973b-682b-4390-9d33-3cb8887cc996.png)
 ![image](https://user-images.githubusercontent.com/44790709/203612006-9040ee7b-af93-41d8-9831-667e7bc0792b.png) 


- This will get the job done, but feels rather slow. Also, if the daemon only prints out the correct password, it feels very impractical, since we'll need to manually search the output ourselves. Lets try a different approach. We'll first create a file containing all password + pincode possibilities.  
 ![image](https://user-images.githubusercontent.com/44790709/203610967-94ab238c-d29a-4fdf-9f3a-16097fb41897.png)

- Then, we'll use cat to read the file and provide it as input to netcat. We can save the results in an output file.  
![image](https://user-images.githubusercontent.com/44790709/203611172-3c430701-7694-48eb-bf25-42fd31d31d40.png)

- We can seach for the passord using grep in our output file. The -v switch allows select all lines that do not match "Wrong"
 ![image](https://user-images.githubusercontent.com/44790709/203611440-48df73a9-6f28-409e-9ea1-070257d03507.png)

- Et voilá
