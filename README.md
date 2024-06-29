# This is leetcode problem to find possile longest palindrome that can be built from the string
# Note: the output will be a integer


# To return the length of the longest palindrome that can be built with the given string
 eg:
 input:abccccdd
 output:7
 Here there are four "c" and two "d" and one "a"  and one"b".
 we can either create "dccaccd" or "dccbccd"longest palindrome and returning it length which is 7.

 # I used a dictionary to store the frequencies of the each letter in the string .if the frequency divided by 2 equal to zero. we can store frequency.if it is odd we reduce it frequency by 1 and 
 # add to result and set true to flag and return the result.
 
 
