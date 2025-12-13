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
        if n==1:
            print(""" Your Choice 
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """)
        elif n==2:
            print(""" Your Choice 
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)
                ---.__________)
                """)
        elif n==3:
            print(""" Your Choice 
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

        if com==1:
            print(""" computer Choice 
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """)
        elif com==2:
            print(""" computer Choice  
                     _______
                ---'    ____)____
                           ______)
                          _______)
                         _______)
                ---.__________)
                """)
        elif com==3:
            print(""" computer Choice 
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
        print(f"User: {user} Computer: {com}")
        W_c(user,com)
    except :
        print("Enter valid Number")
        continue
        