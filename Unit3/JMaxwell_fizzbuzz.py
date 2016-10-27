swaggy = int(input("Enter a number to start at: "))
P = int(input("Enter a number to end at: "))

for x in range(swaggy - 1, P):
    x = x + 1
    if x % 3 == 0 and x % 5 == 0:
        print ("fizzbuzz")
    elif x % 3 == 0:
        print ("fizz")
    elif x % 5 == 0:
        print ("buzz")
    else:
        print (x)