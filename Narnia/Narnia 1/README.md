# Narnia Level 0 → Level 1
 
## LEVEL GOAL
There is no information for this level, intentionally.

## SOLUTION

- We first travel to our dir of interest to find out multiple binaries along with their respective source code. To this challange, we're interested in looking at narnia0 binary and the respective narnia.c. We run the binary and take a peak at its source code to find some interesting details                                                 
 ![image](https://user-images.githubusercontent.com/44790709/203798385-feae6f99-5763-4cd1-a931-f18bb14ac331.png)

- It seems we're asked to change the value of a variable to *x0deadbeef*. From the source code, we see that a buffer of 20 characters is created and then scanf reads it for input. However, scanf is later used for the scanning of 24 characters.
This allows us to overflow our buffer and change the values of the memory address immediatly after the ones reserved for our buffer.
In other words, we can fill our buffer with random data and we'll still be able to fill an extra 4 bytes of memory, which is where our *val* is stored.
This is how we'll be changing the values of *val*. Lets make a quick attempt                                       
 ![image](https://user-images.githubusercontent.com/44790709/203796725-b2dd3c9f-17b7-45ea-9dd0-771c5915839b.png)

- Our theory is proven right. We are able to change the value of *val* by overflowing the buffer. Lets try use shellcode now
![image](https://user-images.githubusercontent.com/44790709/203796988-02e3d3d7-c5bc-40ad-93c8-b03754ef7a25.png)

- We sort of nailed it... We managed to change *val* to the correct value, but not get a shell, as the program terminates right away. We can try using groups of commands:
 ![image](https://user-images.githubusercontent.com/44790709/203797992-e3b16b15-d765-4047-b477-041a933a3c41.png)

- Et voilá   
