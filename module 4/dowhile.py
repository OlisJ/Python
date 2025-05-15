while True:
    user_input=input('Enter a pozitive number:')
    if user_input.isnumeric():
        number=int(user_input)
        if number>0:
            break
    print("invalid imput Please try again")
print('Youve enetered a valid postive number:', number)