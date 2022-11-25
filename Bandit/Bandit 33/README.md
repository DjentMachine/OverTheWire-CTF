# Bandit Level 32 → Level 33
 
## LEVEL GOAL

After all this git stuff its time for another escape. Good luck!

## SOLUTION

- It seems our default shell is once more a strange one. As soon as we log in, we get a message saying 'Wellcome to the uppercase shell'. Just as the name implies, anything we type into is converted to upper cases. This might be a bit of a problem, since at a first glance, we have no way of inputing shell commands.                                   
 ![image](https://user-images.githubusercontent.com/44790709/203985530-54d67ced-002b-458f-acc2-365f453df4de.png)

- Lets try using positional parameters. That is, parameters ranging from $0 to $9. As their name implies, these variables correspond to different values within a Bash script depending on their positions. The $0 special variable serves two different purposes depending on context: if called within a Bash script, it prints the name of the script; if called from the terminal, it displays the name of our shell. Lets check the name of our shell                                                                                                                     
 ![image](https://user-images.githubusercontent.com/44790709/203985690-d46ea8bf-7209-46d1-a027-2f49ab5269a7.png)

- It seems we have a shell... could it be that easy?                                                                         
 ![image](https://user-images.githubusercontent.com/44790709/203985842-d8335399-7744-42fa-881c-d994f725a737.png)

- Et voilá
