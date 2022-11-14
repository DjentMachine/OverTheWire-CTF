# Behemoth Level 0 → Level 1

## LEVEL GOAL

There is no information for this level, intentionally.

## SOLUTION

- Our MD will change for these challanges. First we go to the /behemoth/ location as intructed. We can find a few SUID files. I rekon there's 1 SUID file for each level, so lets try to exploit the behemoth0 file.
 ![image](https://user-images.githubusercontent.com/44790709/201650224-7f218f13-cdfa-418a-9aca-354fde3ad2af.png)
 
 - Using ltrace on our file allows us to see strcomp being use once more to a hardcoded string. Lets use that string as a password and see what happens
  ![image](https://user-images.githubusercontent.com/44790709/201650519-0cbf7b55-666e-467d-88c2-c1dd29128b77.png)
  
  - We are granted a shell as Behemoth 1! Lets get the password file from the /etc/pass directory
  ![image](https://user-images.githubusercontent.com/44790709/201650941-e844754c-ecd4-4ecc-a6f8-c7eb0a7340ba.png)
  
  - Et voilá


