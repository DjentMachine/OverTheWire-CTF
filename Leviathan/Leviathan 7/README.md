# Leviathan 7
 
## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- Pry on the home dir using ls once more:                                               
 ![image](https://user-images.githubusercontent.com/44790709/201445470-19388e94-ac7c-407c-a4c3-91b568996956.png)

- Another SUID file. This time, ltrace tells us that the program expects a 4 digit code and ends its function if its not the correct one.
 ![image](https://user-images.githubusercontent.com/44790709/201446238-c8b6a6ac-c4ff-4bbe-8af4-915aa6447cf8.png)

- It seems like a simple bruteforcing problem. Lets first try bruteforcing numbers 1000 to 9999: 
 ![image](https://user-images.githubusercontent.com/44790709/201446577-50802288-a646-41ea-9572-8171ea7025d9.png)

- Eventually, at iteration number 7123 it seems something changed: we are granted a shell. 
 ![image](https://user-images.githubusercontent.com/44790709/201446361-d45323a6-5071-4ef9-ac9d-61a4d15e1425.png)

- It seems we have the privileges to print out the password at /etc/pass!                        
 ![image](https://user-images.githubusercontent.com/44790709/201446540-1edd2e71-e956-46d2-bdcb-d39bba97b528.png)

- Et voilá
