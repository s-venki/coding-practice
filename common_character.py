from collections import Counter
def main():
   i=input("Enter the list:")
   s=i.split(',')
   print(character(s)) 
    
def character(s:list[str]):
     # Initialize common_character_counts with the characters from the first word
    common=Counter(s[0])
    
    res=[]
    for i in range(1,len(s)):
           # Count characters in the current word
          current=Counter(s[i])
            # Update the common character counts to keep the minimum counts
          for letter in common:
               common[letter]=min(common[letter],current[letter])
    # Collect the common characters based on the final counts         
    for letter,count in common.items():
           for _ in range(count):
                 res.append(letter)   
    return res                   

if __name__=='__main__':
      main()