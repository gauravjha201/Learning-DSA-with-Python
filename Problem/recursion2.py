

# def struct(n):
#     for i in range(1,n+1) :
#         print("*"*(n-i+1))


# struct(4)


# this by recursion
def pattern(n):
    if(n==0):
        return 1
    print ("*"*n)
    return pattern(n-1)

pattern(4)
