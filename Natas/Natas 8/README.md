# Natas Level 7 → Level 8

Username: natas7 <br>
URL:      http://natas7.natas.labs.overthewire.org

## SOLUTION

- When we log in, the website allows us to travel to 2 other pages, home and about. Checking the source code, we see a hint: the path where our password lies.   

 ![image](https://user-images.githubusercontent.com/44790709/206319361-3e791a23-33e8-4140-bcb4-bebe99457572.png)

- If the password lies in the /etc/ folder, we shouldn't have access to it. However, looking at the URL of the website while changing between home and about pages, we see something that screams file inclusion vulnerability.

 ![image](https://user-images.githubusercontent.com/44790709/206319732-076af27b-726d-4540-aae1-95b98c4f29a1.png)

- It seems php is using the variable *page* to load each page. We could try to access something we aren't suppose to using this variable. Lets try setting this var to the path where our password lies.  

 ![image](https://user-images.githubusercontent.com/44790709/206319049-94fb1346-563b-4b59-83b3-933ca3267a0a.png)

- Et voilá
