# Bandit Level 20 → Level 21
 
## LEVEL GOAL
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument.
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20).
If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

## SOLUTION
- For this challange we have to find a way to use the provided suid file. At a first glance, it seems we should set up a listener using netcat, and immidiatly provide the password once the listener has a connection. We could do this over a tmux session in split view.
Lets start by summoning tmux  
 ![image](https://user-images.githubusercontent.com/44790709/203401129-18ca1c77-9d40-4edc-b30d-7dac5b3d747d.png)

- Now we can use Ctrl-b-" to enter the horizontal split view. This way, we can have multiple interactions with the same session. We can switch between screens with Ctrl-b-up/down                                          
![image](https://user-images.githubusercontent.com/44790709/203401507-f20397c7-b912-43b9-9125-2f37413c9cae.png)

- Now let us set a listener using netcat                                                                      
![image](https://user-images.githubusercontent.com/44790709/203401946-3db9b3bb-7c03-4d5b-8fe1-604c08142aa6.png)

- And now we can run the setuid binary                                                                              
![image](https://user-images.githubusercontent.com/44790709/203401995-9512820f-ec79-4fcf-b9ab-971852d3e8f0.png)

- Finally, we go back to the listener and just write the password                                       
 ![image](https://user-images.githubusercontent.com/44790709/203402131-414ce34b-6ca0-4f2e-8880-d13e824e99b4.png)

- Et voilá
