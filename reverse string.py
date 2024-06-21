#reverse the string using two way pointer

s=list(input())
def reverseString( s: list[str]):  
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
reverseString(s)            
print("reverse string :",''.join(s) )