# The problem is to replace the words in the sentence with the root word in the list
eg;
 input : 
 root words: cat rat bat
 sentence: the cattle was rattled by the battery

 output:
 the cat was rat by bat

 # Method:
  simple ,first get the input from the user accept both root word and the sentence.next sort the root word in the length order.Next,we will make nested loop to check each word in sentence is presnted in the root word
  if word is present swap it with root word and break it ,then we will go to next iteration,until the sentence is completed.
  finally, return the sentence .

  
