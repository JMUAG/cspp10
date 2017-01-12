import random

def some_list():
    random_list = []
    while True:
        user_input_1 = input("Enter a number, Sum, Clear, Print, Length, or Exit: ")
        if user_input_1 == "clear" and type(user_input_1) == str:
            random_list == []
            print (random_list)
        elif user_input_1 == "sum" and type(user_input_1) == str:
            random_list = int(random_list)
            print (sum(random_list))
        else:
            user_input_1 = int(user_input_1)
            random_list = random_list.append(user_input_1)
            print (random_list)
            
            
some_list()