# Leviathan 6 
 
## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION
- Lets use ls once more to see what we have                                                  
 ![image](https://user-images.githubusercontent.com/44790709/201444353-89a67aab-b365-4e5f-a243-9b6a9ef27a16.png)

- We find yet another SUID file which aparently tries to open a non existing file. What happens if we create such file?
 ![image](https://user-images.githubusercontent.com/44790709/201444545-619d2c0d-73e9-4f14-93f0-052bd0ee8431.png)

- Not much to work with. What if the file is not empty?           
 ![image](https://user-images.githubusercontent.com/44790709/201444961-5cf369ad-0b65-4c36-ab5d-25844bb0db30.png)

- It seems putchar is being used to print out the contents of the file. We could exploit this to print out the contents of out /etc/pass file. Lets try using a symbolic link named file.log, as it is what the program looks for
 ![image](https://user-images.githubusercontent.com/44790709/201445106-35eca960-d769-445e-b854-4ea5014e7a94.png)
  
