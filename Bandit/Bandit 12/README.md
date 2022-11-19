# Bandit Level 11 → Level 12
 
## LEVEL GOAL
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

## SOLUTION

- Data.txt is an hexdump of a compressed file. This means we should be able to reverse the hexdump using xxd -r option. We first need to make our temp dir and copy our file there.
 ![image](https://user-images.githubusercontent.com/44790709/202819752-0a34afe7-f434-4105-b6ed-0a73d259088d.png)

- It seems we found ourselves a gzip data. We can try to decompress it to see what happens. However, first we need to change the suffix to .gz, otherwise gzip will ignore it                 
![image](https://user-images.githubusercontent.com/44790709/202819947-38d36f1e-ca44-4c73-9121-8172c6c0ecc3.png)

- Another compressed file. This time a bzip2. We can do the same and see where the rabbit hole goes                            
 ![image](https://user-images.githubusercontent.com/44790709/202820183-f0382ecb-46b0-4127-b092-0c4e568b63cb.png)

- Yet another compressed file... we continue on our path                                                                                     
 ![image](https://user-images.githubusercontent.com/44790709/202820260-478d77b4-209a-4bc9-8ac8-997856c36b73.png)

- Its a tar file now. The syntax changes a bit but the logic is simillar. We want to decompress the file. However, the decompression saga does not ended here. I repeated the previous steps and after around 9 decompressions we finally get an ASCII file which contains the password
 ![image](https://user-images.githubusercontent.com/44790709/202821769-33c5dca2-e856-4bdd-8332-9122f62fc57c.png)

- Et voilá
