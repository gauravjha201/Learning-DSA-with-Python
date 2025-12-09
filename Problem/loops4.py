n=int(input("Enter any number: "))
if(n==2):
     print(f"{n} is prime")

for i in range(2,n):# last index of range function is not included(like n)
     if(n%i)==0:
          print(" Not prime")
          break
else:   
     print("Prime") 
    
    
