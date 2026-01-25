
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def get_prime(num):
    prime_nums=[]
    for i in range(2,num+1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums

print(get_prime(20) )




