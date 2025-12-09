# def sum(n):
#     # this is base condition of recursion
#     if n==0:
#         return 0
    
#     return n+ sum(n-1)

# print(sum(10))


def factorial(n):
    if n==1 or n==0 :
        return 1
    
    return n*factorial(n-1)

print(factorial(5))