# Leviathan 4

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- Why change a winning formula? ls it is!                  
![image](https://user-images.githubusercontent.com/44790709/201260212-e2b11951-2683-4469-b575-986b0c483c66.png)

- We find ourselves another SUID file. Lets check what it does using ltrace
 ![image](https://user-images.githubusercontent.com/44790709/201260337-d1a6d485-73b3-477f-822a-3e0a994957d2.png)

- Again, strcmp is used to compare our input to something hardcoded. What if we give the harcoded string as input?
 ![image](https://user-images.githubusercontent.com/44790709/201260624-27ef03ed-c415-4f40-9c54-3f380144315d.png)

- Et voilá
 
