f=int(input("Enter temprature in F: "))

def convert():
    c=(f-32)*5/9
    return c


print (f"{convert()}C")