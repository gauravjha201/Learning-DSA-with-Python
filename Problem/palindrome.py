n = int(input("Enter the three digit number that you want to check palindrome: "))

def palindrome(n):
    a = 0
    temp = n
    while temp != 0:
        d = temp % 10
        a = a * 10 + d
        temp = temp // 10
    if n != a:
        print("Number is not Palindrome")
    else:
        print("Number is a palindrome")

palindrome(n)


