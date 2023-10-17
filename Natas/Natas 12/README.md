# Natas Level 11 → Level 12

Username: natas11 <br>
URL:      http://natas11.natas.labs.overthewire.org

## SOLUTION

- After a quick log in, we can now change the background colour of our page. Our first hint lies on cookies being protected by XOR encryption. Furthermore, we are once again offered the oportunity to peak into the source code which gives us some interesting findings:

![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/b19c15d5-2ccd-4023-8c40-1d0c1d209de3)

- Reading bottom from top, our code appears to edit cookie information. Before doing so, our information is:
   - encoded as a JSON, 
   - XOR encripted,
   - encoded as base64
     
 ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/b59ceb12-60e2-401f-825e-e7580eed1c7f)

- However, before saving any data the program seems to load a default array which sets a "showpassword" to "no" and "bgcolor" to "#ffffff.
- This loadData() function seems to be . This also strongly suggests that $_COOKIE is storing the encoded and encrypted values of "showpassword" and "bgcolor"     
- It seems our course of action is to change the attribute "showpassword" of $_COOKIE to "yes".
- Lets see what's saved in our cookie:
  
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/538d0ec5-04ba-490e-b5ac-3115175e1df1)

- It seems like a long encrypted string, probably the result of loadData(). Lets look at our xo encryption function:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/e28bbe73-56dc-4abe-a01b-e9f0d9ab9573)

- The provided xor_encryption function shows a hardcoded key. An interesting property of xor encrypton can be summarized as following:
   - plain tex + key = encrypted text
   - encrypted text + key = plain text
   - plain text + encrypted text = key  

- With this in mind, we can try to get our key! We already have the plain text (our default data) so lets work on our encrypted text (cookie data):
   - First we decode it from base 64
     
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/27eafe87-903f-4d58-aadd-d16962e4c8cd)
  - Then we alter our default xor encryption function to accept out encrypted text as a key. Hopefully this will give us our real key:
     ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/3869a3ee-d730-4e27-9b5d-fb76549b5756)

 - There we go! It seems our key is 'KNHL'
    
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/97cb51c6-39ce-4fad-ae47-d9afd41bc89a)

- All we need to do now is to have a plain text conatining "showpassord"="yes", encode/encrypt it, save it as a cookie and we should have our password! Lets get our encrypted cookie to be saved:
- We have our xor encrypted string. Lets encode it with base 64:
  ![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/bfd2f990-70a1-4035-af24-f55831ec964a)

- We are ready to save this string as a cookie using chrome dev tools: 

![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/1b3bad51-fb49-45ef-882d-7120ca8f4d89)

- We set our background to any color and...
   
![image](https://github.com/DjentMachine/OverTheWire-CTF/assets/44790709/b70eb2e5-d343-49ca-bd53-2f1dce051761)

- Voilá
