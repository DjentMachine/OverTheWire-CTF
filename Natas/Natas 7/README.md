# Natas Level 6 → Level 7

Username: natas6 <br>
URL:      http://natas6.natas.labs.overthewire.org

## SOLUTION

- It seems we are now given a way to interact with the server. We are to give a secret as an input. The sourcecode of the script behind the secret validation is available for us to check. Lets do so.

 ![image](https://user-images.githubusercontent.com/44790709/206010773-f7d400c3-70f8-4a6c-a26b-be37b5aeb043.png)

- As expected, when the secret is given, the password is given back. There is an interesting "includes". lets see if we can access it.

 ![image](https://user-images.githubusercontent.com/44790709/206010896-3d6509bf-dc06-4df1-be14-d0c99071d9c0.png)

- We can! So we have the secret. We should get the password now.

 -![image](https://user-images.githubusercontent.com/44790709/206011011-1c87c8e3-8ca6-408f-9ede-e2f3acd16779.png)

- Et voilá
