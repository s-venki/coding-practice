# This is problem to find the length of the the subsquemce after rremoving it from the character taht occured in first squence
It acceepts two strings "first squence" and a "subsuqence" . the "subsquence"  checks for the character that  are not present in the "first squence " in the order and print the  remaining length of the "subsquence."  .
eg :
first squence: coaching
subsquence:coading
output :4

I solved this using greedy two pointer approach.taken two pointer let's say x,y both have a strating value of zero using while loop check if the first character of "subsquence" present in the "first squence".
If it present it shouldincrese the value of x and y by 1 .when loop start again it should strat after the "subsquence"  character in "first squence ". if the subsquence not match the current character we will only 
increase the x by 1. in this way we can find how many character present in the "first squence".we will subtract y with length of the subsquence and give output.

# This is leetcode problem 
I solved it in a .cpp and .py and I will update with .java.

