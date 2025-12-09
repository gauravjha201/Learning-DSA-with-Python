f=open("poem.txt")

content=f.read()

if( "Gaurav" in content):
    print("word present")
else:
    print("word is not present")

f.close()

