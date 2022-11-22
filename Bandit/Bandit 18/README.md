# Bandit Level 17 → Level 18
 
## LEVEL GOAL
There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

## SOLUTION

-  This task is simple enough. We need to use diff to compare the 2 files. It should present us with the different lines
 
 ![image](https://user-images.githubusercontent.com/44790709/203348669-a26064cf-9ca2-4f10-82d7-d4c608373c1e.png)
 
-  Et voilá
