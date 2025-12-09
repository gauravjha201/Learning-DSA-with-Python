

with open("file6.txt","r") as f:
    lines=f.readlines()
lineno=1
for line in lines :
    if ("python" in line):
        print(f"line no. is: {lineno}")
        break
        lineno+=1
        
    else:
        print("Not Found")
