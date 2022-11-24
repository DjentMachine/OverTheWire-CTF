# Bandit Level 31 → Level 32

## LEVEL GOAL
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.

## SOLUTION

- We clone our repository as usual. But this time, printing out the readme file suggests us to push a file... Lets do that
  ![image](https://user-images.githubusercontent.com/44790709/203858095-bd4be060-36a7-4a56-909c-81fee2a1e437.png)

- We create our key.txt file as suggested and proceed with the push: First we add our file to staging. Then we commit it with a message and finally we push it.                     
 ![image](https://user-images.githubusercontent.com/44790709/203858678-52999458-9dec-42ef-8390-22cc0d19a915.png)
 ![image](https://user-images.githubusercontent.com/44790709/203858755-577bb708-764f-4a6c-b301-660984b80a19.png)
 ![image](https://user-images.githubusercontent.com/44790709/203858798-a8b2d81d-0da1-4103-8f82-7124e00fbbe9.png)

- Et voilá
 
