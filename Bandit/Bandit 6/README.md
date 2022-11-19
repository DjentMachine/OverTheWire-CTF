# Bandit 6 → Level 7
 
## LEVEL GOAL

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7

owned by group bandit6

33 bytes in size

## SOLUTION

- We can use a similar MO to the previous challange and use find with the -size, -group and -user tests:
  ![image](https://user-images.githubusercontent.com/44790709/202812675-86718ff0-1491-4129-845f-0d3e39547186.png)

- We find a peculiar file that seems to stand out. Once we use cat, we can get the password!
  ![image](https://user-images.githubusercontent.com/44790709/202812829-dfd1bbc7-3ece-46f4-bdf7-487eb292c91c.png)

- Et voilá
