empty=[]
def add(a):
    empty.append(a)

def odd_even():
    odd_num=[]
    even_num=[]
    for i in empty:
        if i %2==0:
            odd_num.append(i)
        else:
            even_num.append(i)
    print(f"Even number are:{even_num}")
    print(f"Odd number are:{odd_num}")


print("Eneter the 10 numbers:")
for i in range(5):
    n=int(input("enter:"))
    add(n)

print(empty)
odd_even()