'''
1 for snake
-1 for water 
0 for gun

'''

computer=-1
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
comdict={1:"snake",-1:"water",0:"gun"}
younum=youDict[youstr]
print(f"You chose {comdict[younum]}\nComputer chose {comdict[computer]}")

if(computer==younum):
    print("It's draw")

else:   
    if(computer==-1 and younum==1):
        print("You win!")
    elif(computer==-1 and younum==0):
        print("You lose!")  
    elif(computer==0 and younum==1):
        print("You win!")
    elif(computer==0 and younum==-1):
        print("You lose!")
    elif(computer==1 and younum==0):
        print("You win!")
    elif(computer==1 and younum==-1):
        print("You lose!")
    else:
        print("Something went wrong")