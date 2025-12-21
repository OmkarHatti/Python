def Add_Expenses(Expenses,Amount,Category):
    Expenses.append({'Amount':Amount,'Category':Category})

def Display_expenses(Expenses):
    for expense in Expenses:
        print(f"Amount:{expense['Amount']},  Category:{expense['Category']}")

def Total_Expenses(Exepnses):
    return sum(map(lambda expense:expense['Amount'],Exepnses))

def Filter_Expense_By_Category(Expenses,Category):
    return filter(lambda expense:expense['Category']==Category,Expenses)

def Main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')
        if choice=='1':
            amount=float(input("\nEnter Amounnt:"))
            category=input("Enter Category:")
            Add_Expenses(expenses,amount,category)
        elif choice=='2':
            print("\nAll Expenses :")
            Display_expenses(expenses)
        elif choice=='3':
            print("\nTotal Expenses:",Total_Expenses(expenses))
        elif choice=='4':
            category=input("\nEnter Category:")
            expenses_from_category=Filter_Expense_By_Category(expenses,category)
            Display_expenses(expenses_from_category)
        elif choice=='5':
            print("\n\n-----------------exiting program------------------")
            break   

Main()