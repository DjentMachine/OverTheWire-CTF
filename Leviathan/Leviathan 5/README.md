# Leviathan 5

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- Again, lets ls                                                                         
 ![image](https://user-images.githubusercontent.com/44790709/201258371-c1763c03-00f2-4070-85b2-95420e875168.png)

- Something worth looking at the trash?
 ![image](https://user-images.githubusercontent.com/44790709/201258628-c854674f-5479-49b0-a909-98611b7764a5.png) 

- We found some binary information... What happens if we turn this into ascii? Let convert this to ascii using xxd. First, save the info in a string variable 'myVar'. Then, every character in the string s is converted to decimal. We can pipe this into xxd to see the translation
 ![image](https://user-images.githubusercontent.com/44790709/201261027-0a32b570-41d9-4f77-b750-5802dd5bd6c6.png)



- Et voilá
 
 
