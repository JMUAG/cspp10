#Working With Johnson
def some_list():
    random_list = []
    while True:
        user_input_1 = int(input("Enter a number: "))
        if type(user_input_1) != int:
            break
        elif user_input_1 > 0:
            random_list.append(user_input_1)
            print (random_list)
        elif user_input_1 < 0:
            random_list.remove(abs(user_input_1))
            print (random_list)
        elif user_input_1 == 0:
            break

some_list()