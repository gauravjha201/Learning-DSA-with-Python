a=int(input("Enter any  number: "))
b=int(input("Enter any  number: "))
c=int(input("Enter any  number: "))
d=int(input("Enter any  number: "))
if(a>b and a>c and a>d):
    print("a is greater than b , c and d")

elif(b>a and b>c and c>d):
    print("b is greater than a, c and d")

elif(c>a and c>b and c>d):
    print("c is greater than a, b, d")
elif(d>a and d>b and d>c):
    print("d is greater than a, b, c")

else:
    print("Invalid NUmber")