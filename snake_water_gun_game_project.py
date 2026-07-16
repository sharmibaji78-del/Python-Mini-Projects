import random

'''
snake= 1
water =-1
gun= 0'''

computer=random.choice([1,-1,0])
youstr=input("Enter your Choice:")
youDict= { "s" : 1, "w":-1 , "g":0}
reverseDict= {1 : "snake", -1: "water" , 0: "gun"}

you = youDict[youstr]

#By now we have two  numbers(variables), you and computer

print(f"you chose {reverseDict[you]} \n computer chose {reverseDict[computer]}")

if computer==you:
    print("It's a draw")
else:
    if computer==-1 and you==1: 
        print("You Win!")
    elif computer==-1 and you==0: 
        print("You Win!")
    if computer==1 and you==-1:
        print("You Lose!")
    if computer==1 and you==0:
        print("You Win!")
    if computer==0 and you==1:
        print("You Lose!")
    if computer==0 and you==-1:
        print("You Lose!")
    else:
        print("Something went Wrong.")