# Leviathan 1

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- As always, lets see what we were given to work with using ls
 ![image](https://user-images.githubusercontent.com/44790709/201243634-b52cc05a-a074-46cf-8cac-c98e4d5666d4.png)

- A SUID file is always a good start of some previlege escalation. But what does it do?                        
 ![image](https://user-images.githubusercontent.com/44790709/201244152-592de533-81b5-4efe-8aaa-2fcf1df862ae.png)

- It seems we are asked for a password and greeted goodbye if we fail. Lets check what is really happening behind the screens using ltrace
 ![image](https://user-images.githubusercontent.com/44790709/201243857-b1486122-0164-4da1-8367-13ad27474bc8.png)

- It seems we strcmp is comparing the first 3 characters of our input with a well known 3 word letter. What if we match our input?
![image](https://user-images.githubusercontent.com/44790709/201244370-6bc31cf1-da25-4666-a031-a544682aa83b.png)

- We have managed to start a shell with escalated previlleges! Maybe now we can access the password stored in /etc ?
![image](https://user-images.githubusercontent.com/44790709/201244614-aa7c649e-d0bf-4913-ae30-81831a79878c.png)

- Et voilá
 
