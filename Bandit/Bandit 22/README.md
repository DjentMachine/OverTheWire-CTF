# Bandit Level 21 → Level 22
 
## LEVEL GOAL

A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## SOLUTION
- We travel to the cron.d dir to find a few cronjobs there. We cat the contents of each file by order, trying to see what kind of processes are scheduled to run. Once we hit cronjob_bandit22.sh, we see that the job is using cat on the password file.
 ![image](https://user-images.githubusercontent.com/44790709/203564830-66c56426-0bc1-404d-9f53-54add2e910bc.png)

- Et voilá
