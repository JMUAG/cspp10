print ("Welcome to The Number Game.💯😂😂😂💯😁")
import random
correct_random_number = random.randint(1,101)
number_of_tries = 0
choice_of_answer = -1
while choice_of_answer != correct_random_number:
    number_of_tries = number_of_tries + 1
    choice_of_answer = int(input("Enter a number: "))
    if choice_of_answer > correct_random_number:
        print("Too high... 📛📛📛 Enter another number: ")
    elif choice_of_answer < correct_random_number:
        print("Too low... ⛔️⛔️⛔️ Enter another number: ")
print ("You got the answer! It took you {} guesses to get the answer👍👍👌. You are a MLG if you got it on the the first 3 tries😱😱😱. If not then play it again untill you get it right...😡😡😡😡👿".format(number_of_tries))

