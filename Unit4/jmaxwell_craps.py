import random

# function name: amount_of_cash
#   purpose: holds the value of the amount of cash you start out with
#   arguments: none
#   returns: the amount of money you have to start the game
def amount_of_cash():
    player_cash = 100
    return player_cash
    
# function name: roll2dice
#   purpose: generating two random dice rolls and 
#           prints it out, and returns the sum
#   arguments: none
#   returns: the sum of the two dice
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print("Rolled 2 dice: {} {}\n".format(dice1,dice2))
    print ("This is a {}".format(dice1 + dice2))
    return dice_sum
# roll2dice()

# function name: first_roll_result
#   purpose: get the result of the first roll
#   arguments: roll_1 - the sum of the two dice rolled on first round
#   returns: the result
def first_roll_result(roll_1):
    if roll_1 == 7 or roll_1 == 11:
        return "win"
    elif roll_1 == 2 or roll_1 == 3 or roll_1 == 12:
        return "lose"
    else:
        return "point" 

# function name: second_roll_result
#   purpose: get the result of the second roll
#   arguments: roll_2 - the sum of the two dice rolled on second round
#   returns: the result of the second roll
def second_roll_result(roll_2,point):
    if roll_2 == 7:
        return "lose"
    elif roll_2 == point:
        return "win"

# function name: bet_1
#   purpose: get the amount of money the player is betting
#   arguments: cash - the amount fo money being bet
#   returns: The amount of money the player is betting
def bet_1(cash):
    cash = int(input("How Much Money Would You Like to Bet? "))
    while cash < 101:
        if cash <= 100:
            return cash
        elif cash >= 100:
            break
bet_1(cash)       
# function name: bet_2
#   purpose: get the amount of money the player is betting after the first round of betting
#   arguments: cash_2 - the amount of money being bet the second time
#   returns: The further of money the player is betting until they quit or loose
def bet_2(cash_2):
    cash_2 = int(input("How Much Money Would Y"))
    
    