# Bandit Level 29 → Level 30
 
## LEVEL GOAL

There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29.

Clone the repository and find the password for the next level.

## SOLUTION
 
- Once more, we create a tmp folder and clone the target repository. We have yet another readme file, but this time, no passwords are in production
 ![image](https://user-images.githubusercontent.com/44790709/203854105-aa0f4e2b-5cd6-4650-89d7-69e01995b98e.png)
 
- We should try to look the commit history once more, although I get the feeling this will be a longshot. 
 ![image](https://user-images.githubusercontent.com/44790709/203854210-feb76108-6105-4434-83d4-6e607084f692.png)
 ![image](https://user-images.githubusercontent.com/44790709/203854253-e31d6caf-dabd-4239-ada4-08a2047aee9f.png)

- No hardcoded passwords in previous commits. But readme speaks of "production". Could there be different branches?  
 ![image](https://user-images.githubusercontent.com/44790709/203856848-76f8567b-afad-4555-b52f-b7062419ee3a.png) 

- There are multiple branches! Lets check /dev... if there are no passes in production there might be some in development
 ![image](https://user-images.githubusercontent.com/44790709/203857155-e5b9f766-e4a4-43aa-83df-7f672cac3ff0.png)

- We have our origin/dev branch checked out. Lets try to cat our new README file
 ![image](https://user-images.githubusercontent.com/44790709/203857229-d18926fb-0f6d-460e-b031-ef6a09a57249.png)

- Et voilá 
