# num = int(input("Enter a number after 15: "))
# for x in range(1,num+1):
    
#     print(x)
# print(num)
# if 



i = input("Enter any number after 15: ")
n = int(i)
for x in range(1,n):
    if x % 3 == 0:
        print ("fizz")
    elif x % 5 == 0:
        print ("buzz")
    elif x % 5 == 0 and x % 3 == 0:
        print ("fizzbuzz")
    print (x)
    