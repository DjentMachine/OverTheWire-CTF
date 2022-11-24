# Bandit Level 28 → Level 29
 
## LEVEL GOAL
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.

## SOLUTION

- We use the same MO as the previous challange and clone the repository into our temp. We then find another readme file which prints the following:
 ![image](https://user-images.githubusercontent.com/44790709/203846963-e98c0321-9330-4dcb-8380-b6a3f1c4b171.png)

- Lets check what type of commits have been made in this repository      
 ![image](https://user-images.githubusercontent.com/44790709/203850244-3e4ce900-64c5-495c-8acc-95ca69728262.png)
 
- There is a commit which states 'add missing data'. This seems promissing enough to take a peek
 ![image](https://user-images.githubusercontent.com/44790709/203851346-909d1ead-bc2b-462f-b78d-57c43c0d5e26.png)

- Et voilá
