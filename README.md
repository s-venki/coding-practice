# This is a problem to check whether the given cards(which is a array) can be arranged in a groups (accept a integer and check how whether the given cards can be arranged in that many consecutive groups).
NOTE:
eg:Input: cards=[1,2,3,6,2,3,4,7,8], groups=3
OUTPUT:true
Explanation: [1,2,3] [2,3,4] [6,7,8] Here 3 groups can be arranged from the given list  and groupsize.

eg:INPUT: cards=[1,2,3,4,5] groups=4
OUTPUT: false
Explanation:we can't arrange the cards into the specified groups because the card list has 5 values and the groupsize should be 4 .(that is [1,2,3,4] [5]) .we can't able to make a consecutive groupsize in the 
first
example here we  have one group has 4 values,while other has one value which is not possible.


# How i solved this program(Basically learned from leetcode solutions 😁)
To solve this problem, we can count the occurrences of each card value in the hand and then iterate through the sorted list of card values, ensuring that each consecutive sequence forms a valid group.
The first step is to check if it's even possible to evenly distribute the cards into groups of size groupSize. We do this by verifying if the total number of cards is divisible by groupSize. 

If not, it's impossible to rearrange the cards, and we can immediately return False.

Next, we count the occurrences of each card value in the hand using a map. Knowing the frequency of each card value will allow us to check if we have enough cards to form consecutive groups.

We create a min-heap containing the unique card values from the hand to maintain the sorted order of the card values. Another option is to sort the map or use a map implementation that maintains sorted order.

We then iterate through the min-heap and extract the smallest card value (currentCard) at each step. For each extracted value, we check the hand to see if it has a consecutive sequence of groupSize cards 
starting from currentCard. We do this by checking if all the card values in the range [currentCard, currentCard + groupSize - 1] are present in the frequency map and have enough occurrences to form a group.

If any of these cards are missing from the count or have exhausted their occurrences, it means the hand cannot be rearranged into the desired groups, and we return False.

However, if all consecutive sequences form valid groups, we can conclude that it's possible to rearrange the cards, and we return True.

The condition "if currentCard + i not in hash map" enhances the solution's efficiency. It allows the function to terminate early when a required card for forming a group is absent. This prevents unnecessary 
decrement operations and subsequent checks, thus optimizing the overall performance to some extent.

# short story 
i only understand the problem but i didn't write the solution in my own words because the the time is 23:53 and iam tired.
it can be a drawback when you don't write the solution in your own words because ultimately the aim is to understand the program. It can be only done through hands on practice like writing for me.
For now, i copy and paste the solution but i will rewrite in my own words.
