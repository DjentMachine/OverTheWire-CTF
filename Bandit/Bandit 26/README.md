# Bandit Level 25 → Level 26
 
## LEVEL GOAL
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

## SOLUTION

- At a first glance, this . We are immidiatly kicked out as soon as we loggin with no further explanation. Apparently, the hint lies on the shell used for user bandit 26. lets check which shell is associated with bandit 26                                    
 ![image](https://user-images.githubusercontent.com/44790709/203622061-50959ad2-d130-4f73-abb3-c3d5a13f8659.png)

- Apparently, a command, more, is executed on a file, text.txt, as soon as we enter. 'more' is known to allow Vim being called, which can be used to execute code. Maybe we can try to do this. There is a caveat though... 'more' will try to read text.txt but will will do it in one go since the content of the file is very little. 'more' skips the need to go into interactive mode, and the session closes as soon as more finishes it's job. We can force more into its interactive mode by decreassing the size of our window.
 ![image](https://user-images.githubusercontent.com/44790709/203626211-e6129bdd-3d05-4317-9833-d950ac047743.png)

- With this interactive mode, we can now call vim by pressing V. We can now return to our normal sized window.                                                  
 ![image](https://user-images.githubusercontent.com/44790709/203626395-90907fe8-9d52-4002-b657-e461da1a90d0.png)

- We should now be able to call a shell. However, before doing so, we should set our shell to /bin/bash, otherwise we'll end up with the 'showtext' shell from before                                                                  
 ![image](https://user-images.githubusercontent.com/44790709/203626759-fda410ce-e78a-4d54-a69e-c29a2e4c9d50.png)
 
 - We can start a shell, and print out the password for this level!                                                                                          
  ![image](https://user-images.githubusercontent.com/44790709/203627122-97fa777b-baff-4ac9-a41a-7e342638876e.png)
  
 - Et voilá
