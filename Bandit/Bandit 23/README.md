# Bandit Level 22 → Level 23
 
## LEVEL GOAL
A program is running automatically at regular intervals from cron, the time-based job scheduler. L
ook in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. 
The script for this level is intentionally made easy to read. 
If you are having problems understanding what it does, try executing it to see the debug information it prints.

## SOLUTION

- We travel to our cron.j dir once more and print out the contents of cronjob_bandit23. We see that a shell script is being run so we print out that .sh as well. It seems the password for the next level is being printed to a temporary file. The catch is: the name of the file is being encrypted with a md5sum.                    
 ![image](https://user-images.githubusercontent.com/44790709/203568856-09d9b8d4-24bf-4329-808f-c99fcbc303fd.png)

- All we need to do is use md5sum on the exact same sentence that is being used to find out the name of our temporary file.                    
 ![image](https://user-images.githubusercontent.com/44790709/203569771-70c53f62-6240-4352-859d-97d53b466719.png)

- Et voilá
