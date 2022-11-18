# Bandit 8
 
## LEVEL GOAL

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

## SOLUTION

- Since the data.txt file is filled with repeating lines of the same size, we should first sort it and then delete the repeated lines. We can first use sort and then pipe the result into uniq using the -u flag
 ![image](https://user-images.githubusercontent.com/44790709/202814374-fbb659a5-86bb-4fb1-8875-0858883f5d2f.png)

- Et voilá
