def ciper(message,key,direction=1):
    key_index=0
    alphabet='abcdefghijklmnopqrstuvwxyz'
    final_message=''
    for char in message.lower():
        if not char.isalpha():
            final_message+=char
        else:
            key_char=key[key_index%len(key)]
            key_index+=1

            offset=alphabet.find(key_char)
            index=alphabet.find(char)

            new_index=(index+offset*direction)%len(alphabet)
            final_message+=alphabet[new_index]
    return final_message

def encrypt(message,key):
    return ciper(message,key)

def decrypt(message,key):
    return ciper(message,key,-1)

while True:
    print("1.Encryption")
    print("2.Decryption")
    print("3.Exit")
    x=int(input("Enter Your Choice:"))
    match x:
        case 1:
            text=input("Enter message You Want To Encrypt:")
            custom_key=input("Enter Key Using Which Yo Want To Encrypt:")

            encryption=encrypt(text,custom_key)
            print(f"Your messege:{text}\nEncrypted text:{encryption}\nkey:{custom_key} (Note:-USe This key for decrypt)")
            continue
        case 2:
            dtext=input("Enter encrypted text:")
            key=input("Enter Key  To Decrypt:")
            decryption=decrypt(dtext,key)
            print(f"Your decrypted text:{decryption}")
        case _:
            print("--------------------Program Exits-------------------")
            break