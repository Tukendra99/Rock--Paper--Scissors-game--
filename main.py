import random
'''
1 for rock
-1 for paper
0 for scissors
'''
computer=random.choice([1,-1,0])
youstr=input("Enter your choice:")
youdict={"r":1,"p":-1,"s":0}
reversedict={1:"rock",-1:"paper",0:"scissors"}

you=youdict[youstr]
print(f"You chose {reversedict[you]}")
print(f"Computer chose                {reversedict[computer]}")
if(computer==you):
    print("Its a Draw")
else:
    if(computer==1,you==-1):
        print("You Win")
    elif(computer==1,you==0):
        print("You Lose")
    elif(computer==-1,you==0):
        print("You Win")
    elif(computer==-1,you==1):
        print("You Lose")
    elif(computer==0,you==1):
        print("You Win")
    elif(computer==0,you==-1):
        print("You Lose")  
    
