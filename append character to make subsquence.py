def main():
   s=input("string 1:")
   t=input("string 2:")
   print(f"output:{append_subsquence(s,t)}")
def append_subsquence(x:str,y:str):
    x1,y1=0,0
    while x1<len(x) and y1<len(y):
      if x[x1]==y[y1]:
         y1+=1
      x1+=1
    return len(y)-y1
if __name__=='__main__':
   main()
       
