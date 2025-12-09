a=5   #swaping by XOR operator
b=10
a=a^b
b=a^b
a=a^b
print(a,b)


#check if the i bit set or not by left operator
# num=1
# i=2
# c=1<<i  #left shift
# d=num&c  #and with number and c
# if d==0000 :
#     print(False)
# else:
#     print(True)


# #check if the i bit set or not by right opertor
# num=13
# i=2
# c=num>>i#right shift 
# d=c&1 #and with 1
# if d==0000 :
#     print(False)
# else:
#     print(True)


# #set the ith bit
# num=13
# i=2
# c=1<<i
# d=num|c
# print(d)

# #clear the ith bit
# num=13
# i=2
# print(num&~(1<<i))


#toggle the ith bit :
# num=13
# i=2
# print(num^(1<<i))


#Remove last set bit 
n=40
print(bin(40))
print(bin(n&(n-1)))
