import random
print ("Welcome to The Number Game 💯😂😂😂💯😁")
print ("Made by Jahseem Maxwell")
correct_random_number = random.randint(1,101)
number_of_tries = 0
choice_of_answer = -1
while choice_of_answer != correct_random_number:
    number_of_tries = number_of_tries + 1
    choice_of_answer = int(input("Enter a number to start: "))
    if choice_of_answer > correct_random_number:
        print("Too high... 📛📛📛 Enter another number: ")
    elif choice_of_answer < correct_random_number:
        print("Too low... ⛔️⛔️⛔️ Enter another number: ")
print ("You got the answer! It took you {} guesses to get the answer👍👍👌.\nYou are a MLG if you got it on the the first 3 tries😱😱😱. \nIf not then play it again until you get it right...😡😡😡😡👿".format(number_of_tries))

