# Natas Level 4 → Level 5

Username: natas4 <br>
URL:      http://natas4.natas.labs.overthewire.org

## SOLUTION

- As soon as we log in we get a message stating we should have come from "http://natas5.natas.labs.overthewire.org" instead of "". This might hint us on the Referer HTTP request header, which gives information on where we come from. 
 ![image](https://user-images.githubusercontent.com/44790709/206006755-1c079507-57e9-4d78-b09c-ba2fd4189fd6.png)

- To test or theory, we installed an chrome addon, ModHeader, which allows us to modify an http header. Lets change or Referer header to "http://natas5.natas.labs.overthewire.org" and see  what happens
![image](https://user-images.githubusercontent.com/44790709/206006670-a121c7b7-8d0b-43cf-ba86-61cca315afa9.png)


- Et voilá
