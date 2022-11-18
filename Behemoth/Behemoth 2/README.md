# Behemoth Level 1 → Level 2

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- We move to our directory of interest and check the file awaiting there for us, behemoth1. We call our programm and are asked a password but we're kicked out immidiatly after. Using ltrace reveals interesting information: Gets function is being called, and Gets is known for being unsafe, as it doesn't check for the size of the input. 
 ![image](https://user-images.githubusercontent.com/44790709/202533352-6865387a-4cea-447f-84d8-d86e95770fdc.png)
 
 - We try to put an unusual long password to prove our theory and we are in luck. The program exits with a segmentation fault. It seems the true challanges start now. We can try to use a buffer overflow and run a shell. This should give us a shell with previleges from Behemoth2
  ![image](https://user-images.githubusercontent.com/44790709/202533720-5e9d1090-beb1-4eb5-afa1-e91dbc7cd1ef.png)

- We use objdump with the -d flag to dissect our program. We find an our main funtion call and take a first look at its dissassembled code.
 ![image](https://user-images.githubusercontent.com/44790709/202535133-1b0f872c-3913-41a0-8d73-ae9669cf4946.png)
 ![image](https://user-images.githubusercontent.com/44790709/202535189-ad2ca038-ddcd-44ed-96a2-215f48d328ab.png)

- For a creating a buffer overflow, we'll need the size of the buffer created in gets and the address at which the buffer starts. We'll check it withwith GDB: first, dissassemble the main function and then add a breakpoint right after the gets function is called.
 ![image](https://user-images.githubusercontent.com/44790709/202536210-5f0714db-9155-44ef-85c9-3cffb65d7f1f.png)
  
- Interesting to note the following line:  
0x08049199 <+3>:     sub    $0x44,%esp 
- This tells us 68 bytes (decimal for 0x44) have been allocated to the stack, **$esp**. This should hint us on the size of our buffer. We'll run the program, give a long password, and take a peek at the adressess shown in the stack. We'll use this with x/200x $esp (e**x**amine 200 he**x**adecimals in the stack)
 ![image](https://user-images.githubusercontent.com/44790709/202536800-2c420bcf-7137-4951-832d-8e0ffe95864d.png)
 
- We got our first milestone, we have found out were our buffer starts: **0xffffd4b0**. This is the top of our stack. We can see our input of A's (\x41 in hexadecimal) starting at this address and going all the way up until we hit our return address, **$eip**, which, if the provided password was long enough should be overwritten with 0x41414141.
 ![image](https://user-images.githubusercontent.com/44790709/202538759-5dcd9d0f-51f5-409f-b9d5-8c1bf88a2b16.png)

- We have confirmed our theory! The return address gets overwritten, which means we can overwrite this to an address that is convinient to us. For now, lets us find where is this address. We can do this by checking where the bottom of stack is. Lets remind ourselves that everytime a function gets called, the base pointer is updated. So by subtracting the base pointer with the stack pointer we should have the amount of memory allocated to our function, and in this case, our buffer
 ![image](https://user-images.githubusercontent.com/44790709/202540593-31b78723-bc4b-443d-ad98-9a431045bf8f.png)

- Our buffer size should be around 72. Lets try giving a password with 72 A's. and 4 extra B's. Our return address should contain x42424242 (hexadecimal for BBBB)
![image](https://user-images.githubusercontent.com/44790709/202545372-b98ecfbe-e813-4f9a-937c-65cbea748530.png)

- It seems we were too deep. We can already see our A's (41's) occupying a new address. Considering there is probably a null byte at the end of the buffer, lets try using 70 A's
 ![image](https://user-images.githubusercontent.com/44790709/202545573-2b46c291-c9d6-4676-b604-bb0106de278c.png)
 
 - Yes! We didn't get a segmentation fault, which means 70 is the buffer size. We also confirm the existance of a null byte at the end of the buffer. 


  
 

