# Natas Level 8 → Level 9

Username: natas8 <br>
URL:      http://natas8.natas.labs.overthewire.org

## SOLUTION

- After log in, we see once more a button for the source page and a secret waiting to be input. Taking a look at the source code, we see a short php script trying to compare our seceret to a hardcoded once. The catch is that before comparison, our secret passes to a series of encoding functions.

 ![image](https://user-images.githubusercontent.com/44790709/206323320-fd352059-1d62-40dd-bd29-36eb5ce76d78.png) 

- First, the secret gets encoded to base 64. Then, the string is reversed. And finally, it's converted to hexadecimal. We should be able to use the same funtions on the hardcoded string, but in reverse order. First, we use hex2bin

 ![image](https://user-images.githubusercontent.com/44790709/206323225-403ff67c-a69b-4eed-958a-ee36544fbcf5.png)

- We can now reverse the string use any online tool once more

 ![image](https://user-images.githubusercontent.com/44790709/206323259-c5a7b42b-31c8-4f7b-a6a6-0328ade30080.png)

- And finally, we get to decode from base 64 and get our secret.

 ![image](https://user-images.githubusercontent.com/44790709/206323164-2d494383-5dfa-4489-af5c-1e70fc0661c4.png)

- Using our secret should provide us the password.

 ![image](https://user-images.githubusercontent.com/44790709/206323436-f0dadce1-0969-44fe-9eae-bb399e77139d.png)

- Et voilá
