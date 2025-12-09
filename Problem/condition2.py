a=int(input("Enter marks of english: "))
b=int(input("Enter marks of math: "))
c=int(input("Enter marks of physics: "))

percentage=(a+b+c)/3

if(percentage>=40 and a>=33 and b>=33 and c>=33):
    print("YOu are pass",percentage)
else:
    print("fail",percentage)
    

