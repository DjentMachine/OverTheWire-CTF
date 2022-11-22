# Bandit Level 18 → Level 19
 
## LEVEL GOAL
The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

## SOLUTION

- When we try to log in we are immidiatly kicked out. It seems like we should cat our readme file in one pipe before our session gets terminated. Lets try to send a command using ssh:
 ![image](https://user-images.githubusercontent.com/44790709/203350993-e518966d-b930-49af-a3b4-05fb8e7f5660.png)

- Et voilá
