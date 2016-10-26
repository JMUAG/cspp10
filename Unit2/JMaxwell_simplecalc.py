expression = input("Please enter an expression: ")
#This will make the reader enter a mathematical equation such as 1 + 1
answer = int(expression[0])
#This makes the 1st number into an interger from a string
answer_2 = int(expression[2])
#This turns the 2nd number into an interger from a string 

if expression[1] == "+":
    print (" The result is " + str(answer + answer_2))
#This is saying if the operation is addition, then to add the two intergers together and then turn the sum into a string
elif expression[1] == "-":
    print (" The result is " + str(answer - answer_2))
#This is saying if the operation is subtraction, then to subtract the two intergers from eachother and then turn the difference into a string
elif expression[1] == "%":
    print (" The result is " + str(answer % answer_2))
#This is saying if the operation is modulo, then to divide the two numbers from eachother, keep the remainder from the two, and then turn the remainder into a string
elif expression[1] == "/":
    print (" The result is " + str(answer / answer_2))
#This is saying if the operation is division, then to divide the two numbers from eachother and then turn the quotient into a string
elif expression[1] == "*":
    print (" The result is " + str(answer * answer_2))
#This is saying if the operation is multiplication, then to add the two numbers together and then turn the product into a string
elif expression[1] == "**":
    print (" The result is " + str(answer ** answer_2))
#This is saying if the operation is an exponent, then multiply the 1st number by the 2nd number's amount of times and then turn the answer into a string
else:
    print ("ERROR")
#This is saying that if the code does not match any of the standards above, then to Print "Error"