# Natas Level 12 → Level 13

Username: natas12 <br>
URL:      http://natas12.natas.labs.overthewire.org

## SOLUTION

- This time around, we are allowed to submit a .jpg file with a max size of 1kb. Before peeking the source code, lets test this functionality and upload a random image:
  
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/a58a4ce0-3c7e-4642-bd81-915a0016c926)

- What if we try any other file?
  
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/05aea711-b168-4dcd-a9e2-6d32e41c2c32)

- We also get an url with the extention .jpg. Looking at the source code sheds light on what is happening on the server:

- genRandomString() does exactly that: it generates a 10 character string. This function is used twice throughout the code. Once to generate a path for our upload and another in our post request, as it sets an atribute value to a randomly generated string with an .jpg hardcoded extention  
 ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/f17b1888-d372-4099-964d-4d02889a3152)
 ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/9e915fad-7259-45fd-b85c-9df174806dc3)

- Reading on through the code we can summarize whats happening as the following:
  - As soon as we create our post request, a random "filename" is created with a .jpg extention. This is independent from the file we uploaded
  - If there is a "filename" in our post request (which should always be the case), we create a random file path based on a 10 character string which the following structure:  upload/XXXXXXXXXX.jpg. This is saved in a $target_path variable.
  - If the file is larger than 1000 bytes, an error is raised
  - If not, the file we uploaded is moved to $target_path. This means our file name is necessarily changed to XXXXXXXXXX.jpg     

- This means that no matter what type of file we upload, it's name and extention will always be changed to XXXXXXXXXX.jpg, and this is given by the "filename" attribute from our post request. Having this type on input on the client side can be dangerous, since we should able to manually edit the content of filename to something convinient and be able to run code.

- We'll need a proxy to intercept our own post request before it reaches the server. We'll use Burp Suit's Intercept to do so and check the contents of our post request:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/214dcefb-1d45-44b9-a64a-ce3ab70ed1d1)

- We can see that the filename attribute was already generated. We can manually edit this, change the extention to .txt and see how this affects the output:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/35d20c85-b130-45ed-a970-53e51e828d3e)

- Now we actually have a txt file being uploaded and we can even check it's contents!
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/36d70345-396a-4cea-87c3-6faceddf8832)
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/be09e7f3-aa05-4499-beeb-d95e96254cff)
- All we need now is to actually upload something that allows us to get the password for the next level. We could try using a .php file which uses "system" to run bash commands such as cat. Something like "<?php echo system(\"cat /etc/natas_webpass/natas13\"); ?>". Lets try this:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/624ce4c9-c9d5-431d-a565-84edf53971be)

- We upload our .php file, "filename" is generated as "rwxwgp5101.jpg", we manually change its extention to .php in burp, and wait for the results:

![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/ca90e230-5a0a-4819-b571-ea3a520b6876)
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/e5fe5076-3357-4be9-93ee-136b9ac45e38)

- Et voilá
