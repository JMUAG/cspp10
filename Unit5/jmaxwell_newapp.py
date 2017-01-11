import random

def some_list():
    random_list = []
    while True:
        user_input = int(input("Enter a number: "))
        if type(user_input) != int:
            break
        elif user_input > 0:
            random_list.append(user_input)
            print (random_list)
        elif user_input < 0:
            random_list.remove(abs(user_input))
            print (random_list)
        elif user_input == 0:
            break

some_list()