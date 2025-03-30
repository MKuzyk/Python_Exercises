'''
Pobieraj znaki z klawiatury aż do wprowadzenia znaku x. Ile znaków pobrano?
'''

def signs():
    char_list=[]
    while True:
        char = input("Input the sing in to the list / If you would like to finish input x :")
        if char == 'x':
            break
        char_list.append(char)
    print(f"Your inputed signs : {char_list}!")
    print(f"You inputed {len(char_list)} sign/signs!")

signs()