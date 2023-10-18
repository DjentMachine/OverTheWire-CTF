# Natas Level 13 → Level 14

Username: natas13 <br>
URL:      http://natas13.natas.labs.overthewire.org

## SOLUTION

- After logging in we find a similar exercice to Natas13, but this time we are warned that the uploaded file must be an image, hinting that some sort of validation to the file is done. Before peeking the source code, lets test this by uploading a text file:
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/71be8b58-bc9d-448a-afc0-1d9a35c14ccd)
- We get a "file not an image" message as expected. We look through the code to find a similar code to natas13 with a new feature: a validation being done by a exif_imagetype() function.

  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/06bc2b69-d59a-4c5b-a0b4-622cbb39ef2e)

- This function looks at the signature of a file to make sure that the input is indeed an image. So in theory, if we change any file's signature to a jpg one, we should be able to bypass this validation. And if so, we could reuse the rationale from Natas13: upload a .php file which uses cat to print out the password saved in /etc/natas_webpass.

- Lets try changing a file's signature. We first create a dummy text file:
 ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/2bc32551-2c0f-44f1-846b-cede053d15e8)

- Fortunatly, wikipedia has a very convinient article on file signatures which tells us the signature of a .jpg file:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/76f00cdf-93d6-4e79-a56b-93f362b2ddd1)

- We can focus on the signature: FF D8 FF E0 00 10 4A 46 49 46 00 01

- Lets try to create a text file with a fake signature. Use use echo with the -n (ignore trailing lines) and -e (allows for interpretation of backlashes) to add our magic bytes to our file. By using -e, our \xHH input will be interpreted as bytes with hexadecimal values. We will be able to change the first bytes of our file to mimic those pf a jpg file signature:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/f7840897-a3e9-4457-a472-055946936d87)

- This worked! Our file is recognized as an image! We can try doing this with our previous php command:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/2cf22063-11d1-4c0c-af5f-0531b589ec8c)

- We upload our file and resume the process with Burp Suit, the same as in Natas13
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/67108f1b-da9f-434a-92b6-ac49fceaee79)

- **Et voilá**

![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/f73a04ad-2df9-4a77-8eb8-889cc0cd8e28)
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/32984224-921b-4704-b610-56303250299a)



