#Working with Johnson
list_1 = [] 
while True:
    user = input("Enter a number, sum , clear , length, exit, print: ").lower()
    if user == "clear":
        list_1 = []
        print (list_1)
    elif user == "sum":
        print (sum(list_1))
    elif user == "length":
        print (len(list_1))
    elif user == "exit":
        break
    elif user == "print":
        print (list_1)
    else:
        list_1.append(int(user))