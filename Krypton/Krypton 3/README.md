# Krypton Level 2 → Level 3
 
## LEVEL GOAL

ROT13 is a simple substitution cipher.

Substitution ciphers are a simple replacement algorithm. In this example of a substitution cipher, we will explore a ‘monoalphebetic’ cipher. Monoalphebetic means, literally, “one alphabet” and you will see why.

This level contains an old form of cipher called a ‘Caesar Cipher’. A Caesar cipher shifts the alphabet by a set number. For example:

plain:  a b c d e f g h i j k ...
cipher: G H I J K L M N O P Q ...
In this example, the letter ‘a’ in plaintext is replaced by a ‘G’ in the ciphertext so, for example, the plaintext ‘bad’ becomes ‘HGJ’ in ciphertext.

The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.

One shot can solve it!

Have fun.

Additional Information:

The encrypt binary will look for the keyfile in your current working directory. Therefore, it might be best to create a working direcory in /tmp and in there a link to the keyfile. As the encrypt binary runs setuid krypton3, you also need to give krypton3 access to your working directory

## SOLUTION

- Since our encrypt file reads from the current directory and outputs a file into the same direcory, we will need to create a tmp dir, otherwise we wouldn't be able to output anything. We then create a symbolic link to our keyfile and test the usage of our encrypt file
  ![image](https://user-images.githubusercontent.com/44790709/202849759-7fbeab41-6c67-4840-9b25-701ad0776951.png)

- Everything is working as supposed. It seems that A's are substituted with M's, B's with N's and so on. Thats a rot-12. So we can use tr once more on the contest of the file krypton3 and see what happens
 ![image](https://user-images.githubusercontent.com/44790709/202849954-958b7e09-c4de-4135-8e58-0933f2deb7fc.png) 
 ![image](https://user-images.githubusercontent.com/44790709/202853121-2b1997f9-a14c-4ead-a58e-6f0bbc378963.png)

- Et voilá
