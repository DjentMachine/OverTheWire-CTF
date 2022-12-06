# Natas Level 5 → Level 6

Username: natas5 <br>
URL:      http://natas5.natas.labs.overthewire.org

## SOLUTION

- We log in, only to find out we ... aren't logged in?

 ![image](https://user-images.githubusercontent.com/44790709/206007637-83c8931c-9e77-48e8-b5d3-88409bf28e5d.png)

- However, while taking a look at the request headers once more, we see a suspicious header: Cookie with a value loggedin=0. Let's change that to =1 and see if it works.

 ![image](https://user-images.githubusercontent.com/44790709/206008927-c873f41c-5d5b-42ed-8c8c-e515fd04b1a5.png)

- Et voilá
