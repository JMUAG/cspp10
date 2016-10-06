expression = input("Please enter an expression: ")
answer = int(expression[0])
answer_2 = int(expression[2])

if expression[1] == "+":
    print (" The result is " + str(answer + answer_2))
elif expression[1] == "-":
    print (" The result is " + str(answer - answer_2))
elif expression[1] == "%":
    print (" The result is " + str(answer % answer_2))
elif expression[1] == "/":
    print (" The result is " + str(answer / answer_2))
elif expression[1] == "*":
    print (" The result is " + str(answer * answer_2))
elif expression[1] == "**":
    print (" The result is " + str(answer ** answer_2))
else:
    print ("ERROR")
    
#number = input("Please enter a number: ")
#operation = input("Please add one operation such as addition: ")
#number_2 = input("Please enter another number: ")
#answer = int(number) + int(number_2)
#print ("The result of " + str(number) + " and " + str(number_2) + " is " + str(answer) )