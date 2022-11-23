# Bandit Level 23 → Level 24
 
## LEVEL GOAL
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script.
This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

## SOLUTION

- Another cronjob challange. We keep the same MO, moving to our cron.d dir and check what is the job associated to Bandit24. We also check which sh file is set to run.                    
 ![image](https://user-images.githubusercontent.com/44790709/203593239-94a43a1b-afcd-4d94-9400-353887662990.png)               

- This sh file executes and deletes all normal (\*) and hidden (.\*) files in a specific folder. This job also runs on Bandit 24 privileges. We can use this job to retrieve our password. We then create a temporary folder and give read/write permissions to everyone                                
  ![image](https://user-images.githubusercontent.com/44790709/203594744-ca790aa8-7f7f-4b51-b64c-a9bd27af8d25.png)
  
- We can also create a sh script that will retrieve the pass from /etc/bandit_pass and outputs it to our temp folder. Afterwards, we set write/read/execute permissions of our sript to everyone                       
  ![image](https://user-images.githubusercontent.com/44790709/203595077-19ef7b06-e8af-4d3c-96c3-0b6911ef7931.png)
  
- All that is missing is to print out the resulting file:                                       
 ![image](https://user-images.githubusercontent.com/44790709/203596022-7ffa19b0-37cf-4dfc-b3bf-9f7c4b3f792e.png)
 ![image](https://user-images.githubusercontent.com/44790709/203596104-5a38775b-2599-4ad5-a099-acfd8b9502f8.png)

- Et voilá
