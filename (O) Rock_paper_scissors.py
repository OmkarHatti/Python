import random

def W_c(user,comp):
    c={
        'Rock':'Scissors',
        'Paper':'Rock',
        'Scissors':'Paper'
    }
    if user==comp:
        print("game is Tie")
    elif c[user]==comp:
        print("You Won")
    else:
        print("Compuetr won")
        
choice=['Rock','Paper','Scissors']
while(True):
    print("\n1.Rock")
    print("2.Paper")
    print("3.Scisors")
    print("4.Stop")
    try:
        n=int(input("Enter Your Choice:"))
        user=choice[n-1]
        if n==4:
            print("You Quit")
            break
        com=random.choice(choice)
        print(f"User: {user} Computer: {com}")
        W_c(user,com)
    except :
        print("Enter valid Number")
        continue
        