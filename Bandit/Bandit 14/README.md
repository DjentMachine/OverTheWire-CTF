# Bandit Level 13 → Level 14
 
## LEVEL GOAL

The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

## SOLUTION

- A simple task: we use ssh with the identity file flag -i. Obviously use provided private key
 ![image](https://user-images.githubusercontent.com/44790709/202872325-4610e672-5d4d-4c4e-94fb-8b1d1160cc2f.png)
