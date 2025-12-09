book={}
book['tom']={
    'name' : 'Tom',
    'address' : 'red street NY',
    'phone' : 900347549
}
book['bob']={
    'name':'bob',
    'address':'green street NY',
    'phone':93745759
}
import json#java Script Object Notation
s=json.dumps(book)
with open("C:\Users\jhaga\OneDrive\Desktop\data\book.txt","w") as f:     
    f.write(s)
# print(s) 
