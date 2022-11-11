# Leviathan 3

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- Our MD stays unchanged: using ls                                                                
 ![image](https://user-images.githubusercontent.com/44790709/201244947-758a34fb-36c6-44de-8f1d-3ab623f30750.png)

- Another SUID file. Judging by its name, I rekon it prints a given file using cat?                             
 ![image](https://user-images.githubusercontent.com/44790709/201245088-321a5795-f492-4bee-ac8d-e0db9dac4d56.png)

- We probably can't print the file for the next level stored in the /etc/ folder but lets try it anyway using ltrace while we're at it
 ![image](https://user-images.githubusercontent.com/44790709/201245248-ebbd82fc-b22c-4c0f-a767-0cf7e7692c90.png)
 
- As expected. Ltrace hints us to the use of access() in the programm. We've learn that using access() to validade whether a file can be read or open can be a vulnerability due to a time gap between the access and the reading/open! Lets see try printing a file we actually own
![image](https://user-images.githubusercontent.com/44790709/201246243-5d6c6491-3bfb-44ed-99d0-87d91cfc1fb0.png)

- In this call, we see cat is indeed used as part of the program, right after access. We might be able to exploit this by tricking cat into reading 2 files!

![image](https://user-images.githubusercontent.com/44790709/201247250-20a5a662-f224-440b-b93b-dde6300fb729.png)

- Cat does try to print 2 files! We can try print the password file at /etc/ folder. We'll do it using a symbolic link. We create a symbolic link to the password file and just try to read it using the smae technique as before by proving 2 files for the cat call 
![image](https://user-images.githubusercontent.com/44790709/201248445-aa8b5aff-9695-4164-b975-b5ef5cbe53f1.png) 

-Et voilá


