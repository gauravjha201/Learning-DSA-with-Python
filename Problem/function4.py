list=["Gaurav","goku","Rohan","an"]
n=[]


def rem(list,word):
    for item in list :
       if not (item==word):
           n.append(item.strip(word))
    return n

print(rem(list,"an"))


