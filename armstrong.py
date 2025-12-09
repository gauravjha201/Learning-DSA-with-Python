n=int(input("Enter the number :"))
num=n
i=len(str(n))
sum=0
while num>0:
    ld=n%10
    sum=sum+(ld**i)
    num=num//10
if sum==num :
    print("Number is ArmStrong")
else:
    print("Not ArmStrong")
