# Krypton Level 3 → Level 4
 
## LEVEL GOAL

Well done. You’ve moved past an easy substitution cipher.

The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker.

However, you have been lucky. You have intercepted more than one message. The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3)

You know the following important details:

The message plaintexts are in American English (*** very important) - They were produced from the same key (*** even better!)
Enjoy.

## SOLUTION

- This challange seems fairly obvious: use the messages to break the cipher. However, doing this by hand seems like a time consuming task. No matter, we move to our directory of interest to find a few interesting files. Reading the HINT files gives us 2 valuable tips: **some letters are more common than others in the english language** and **'frequency analyses'**. Judging from the name, I rekon it referes to counting the amount of times a letter appears in a given text. [Wikipedia](https://en.wikipedia.org/wiki/Frequency_analysis) was kind enought to prove me right.
With this in mind, lets read our files so we can see what we have to work with.
 ![image](https://user-images.githubusercontent.com/44790709/202865509-73fa7cd8-f3c2-4dbf-883b-98c0009a6372.png)

- This feels like a very long text... and the other files are simillar and not smaller. We can start thinking about using frequency analyses on the files we have. We cat the content of all found* files together in a single file to have a larger sample size and count the number of times each letter appears                                        
  ![image](https://user-images.githubusercontent.com/44790709/202855001-face9d61-cd34-4cd1-8212-1b46b5331bf2.png)
          
- We have our top 8 most occurring letters, from 1st place to 8th:<br/>
. Found1 - S C Q J U B G D <br/>
. Found2 - S Q J N U B D G <br/>
. Found3 - S Q J G C N B U <br/>
. Total -  S Q J U B N C G  <br/>

- I decided to check the percentage of the frequency for each letter to have a better visualization which gave us the following table:
 ![image](https://user-images.githubusercontent.com/44790709/202855849-fa98696f-7f52-488e-be48-cdc19206652d.png)

- Something also worth checking besides frequency of letters is the frequency bigrams (e.g 'UN', 'TH'), trigrams ('ABC', 'ATE') and repeated letters (e.g. 'ss', 'tt', etc). Using grep with sort and uniq allows for checking which are the most common pattenrs
Examples (output too large to be shown):
 ![image](https://user-images.githubusercontent.com/44790709/202865791-85a680f9-82c1-40bc-b5d2-23a9c98ee2ce.png)
 ![image](https://user-images.githubusercontent.com/44790709/202859401-3f6f5718-e98c-4061-adc7-8692ad24ee8d.png)

- From analyses simillar to the above and comparing it to the frequencies used in the english language, we get a few insights:
. E is the most frequent letter. In our ciphertext, that is S by a landslide. So most likely S == e <br/>
. JDS is the most commun trigram. This confirms S==e but also gives us D==h and S==e

- We can try so make a few substitutions and see if there is something else we can use:
 ![image](https://user-images.githubusercontent.com/44790709/202865992-71349499-581f-4e96-987f-5cfb33a7c776.png)

- We've made some progress but there is still a long way to go. We can try to search for commonly used words. We'll try to serach for 'here' and 'are', as both use r and could give us an extra word.
 ![image](https://user-images.githubusercontent.com/44790709/202866306-6c576f41-3e4a-48c8-bcba-cdc306b946ca.png)
 ![image](https://user-images.githubusercontent.com/44790709/202866296-134923bc-9166-4a38-a8df-838fbeb8f1da.png)

- 'N' sure does show up as a possibility for R! Lets try substituting that and see if the text becomes any cleared.
![image](https://user-images.githubusercontent.com/44790709/202866346-12d8f831-9a50-4f8b-b3f1-3c2656e98e72.png)

- Alright! It's very likely that N == r, which is an important step forward. After carefull examining the file we can see a few words worth exploring: at the exnd of the paragrath there is a word ending in eath. Could this suggest W == d? We could also probably enter a few spaces to help us read better between know words. And we can try seacrhing for words that we can make with our 5 letters. For instance, we can search for 'there' and 'three'.

- After some time, some induction and trial and error, the pattern starts to emerge:
  ![image](https://user-images.githubusercontent.com/44790709/202866705-c5ed34e2-a571-4fcc-9c5f-d74e90fa77f8.png)

- Eventually, we manage to get all the text decrypted and we finally have our cipher
 ![image](https://user-images.githubusercontent.com/44790709/202866741-c0e37606-87af-469f-a69c-792d88a67b98.png)
 
 - We can finally use our cipher on the krypton4 file and get our password! 
  ![image](https://user-images.githubusercontent.com/44790709/202866826-d42c79ce-a716-4f99-af3d-37f69147975d.png)

- Et voilá


