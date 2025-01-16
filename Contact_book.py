def add(name,contact,path):
    with open(path,'a',) as file:
            file.write(f"{name},{contact}\n")
    
def view_all(path):
    print("\nName Contact")
    with open(path,'r') as file:
        lines=file.readlines()
        for i,line in enumerate(lines,1):
            name,num=line.strip().split(",")
            print(f"{i}. {name} : {num}")
     
def View_by_name_char(name,path):
    print("\nName Contact")
    with open(path,'r') as file:
            lines=file.readlines()
            for line in lines:
                c_name,c_num=line.strip().split(",")
                if c_name.startswith(name):
                    print(f"{c_name}: {c_num}")
                    
def update(name,path):
    with open(path,'r') as file:
        lines = file.readlines()
    with open(path,'w') as file:
        for line in lines:
            o_name= line.strip().split(',')[0]
            if o_name==name:
                new_number=input("Enter New Number:")
                file.write(f'{name},{new_number}\n')  
            else:
                file.write(line)
        print("You Successfuly Updated Number:\n")
        
def delete(name,path):
    with open(path,'r') as file:
        lines=file.readlines()
    with open(path,'w') as file:
        for line1 in lines:
            d_name= line1.strip().split(',')[0]
            if d_name!=name:
                file.write(line1)
            
        
        
def main():
    path=input("Enter Your Existing File Path/Create New File by Extention:")
    while True:
        print("\n1.Add Contact")
        print("2.View All Conatct")
        print("3. Search by Name or alphabet:")
        print("4.Exit")
        n=int(input("Enter Your choice:"))
        match n:
            case 1:
                name=input("\nEnter Full Name:")
                contact=input("Enter contact Number:")
                add(name,contact,path)
                print("Contact Added Successfully\n")
            case 2:
                view_all(path)
                while True:
                    print("\n1.update\n2.delete\n3.None of the Above\n")
                    n=int(input("enter:"))
                    if n==1:
                        name=input("Enter name for update:")
                        update(name,path)
                    elif n==2:
                        d_name=input("Enter name for Delete:")
                        delete(d_name,path)
                        print("You successfully deleted data")
                    else:
                        break
            case 3:
                name=input("Enter First letter/Full name:")
                View_by_name_char(name,path)
                while True:
                    print("\n1.update\n2.delete\n3.None of the Above\n")
                    n=int(input("enter:"))
                    if n==1:
                        name=input("Enter name for update:")
                        update(name,path)
                    elif n==2:
                        d_name=input("Enter name for Delete:")
                        delete(d_name,path)
                        print("You successfully deleted data")
                    else:
                        break
            case _:
                print("You exits")
                break
                   
main()
