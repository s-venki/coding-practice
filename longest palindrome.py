def longpalindrome(prompt:str):
    s=input(prompt)
    frequency={}
    for i in s:
        frequency[i]=frequency.get(i,0)+1
    
    res=0
    flag=False
    for i in frequency:
        if frequency[i]%2==0:
            res+=frequency[i]
        else:
            res= frequency[i]-1
            flag=True

    if flag==True:
        res+=1

    return res                
print(longpalindrome("enter a string :"))
