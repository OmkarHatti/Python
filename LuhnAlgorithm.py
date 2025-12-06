def Valid_Card_Number(Card_num):    
    reverse_card_Num=Card_num[::-1]
    sum_of_odd_digits=0

    odd_digits=reverse_card_Num[::2]
    for digit in odd_digits:
        sum_of_odd_digits+=int(digit)
    sum_of_even_digit=0

    even_digit=reverse_card_Num[1::2]
    for digit in even_digit:
        number=int(digit)*2
        if number>=10:
            number=(number//10)+(number%10)
        sum_of_even_digit+=number
        
    return (sum_of_odd_digits+sum_of_even_digit)%10==0


def main():
    card_number=input("Enter a Your Card Number (seprate With space or -):")
    transform=str.maketrans({'-':'',' ':''})
    card_transform=card_number.translate(transform)

    if Valid_Card_Number(card_transform):
        print("Card Is Valid")
    else:
        print("Card Is Invalid!")

if __name__=="__main__":
    main()