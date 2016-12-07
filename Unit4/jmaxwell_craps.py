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
#   purpose: get the result of the roll
#   arguments: roll - the sum of the two dice rolled
#   returns: the result
#       if roll is 7,11: return "win"
#       if roll is 2,3,12: return "lose"
#       if otherwise: return point
def first_roll_result(roll):
    if roll == 7 or roll == 11:
        return "win"
    elif roll == 2 or roll == 3 or roll == 12:
        return "lose"
    else:
        return "point"
 