# Bandit Level 21 → Level 22
 
## LEVEL GOAL

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## SOLUTION
- We travel to the cron.d dir to find a few cronjobs there. We cat the contents of each file by order, trying to see what kind of processes are scheduled to run. Once we hit cronjob_bandit22.sh, we see that the job is using cat on the password file and outputing the contents to a temporary folder.
 ![image](https://user-images.githubusercontent.com/44790709/203566365-0d92460d-2863-4152-9896-3a123821e4fb.png)
 
- We have a temporary file name. We can try to print its contents and see if the password is there
 ![image](https://user-images.githubusercontent.com/44790709/203566282-e5736f80-a2a6-4c76-ab9e-887d9d98dacf.png)

- Et voilá
