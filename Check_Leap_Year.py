def check_Leap(year):
    if year%4==0:

        if year%100==0:
            return year%400==0
        return True
    return False
    

year=int(input("Enter Your Number:"))
if check_Leap(year):
    print("yes Leap Year")
else:
    print("Not leap year")