import random

# function name : roll2dice
# purpose : for the game to roll two dice
# arguments : none
# returns : the sum of two dice
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2
    print ("This is a {} and a {}.".format(dice1,dice2))
    print ("This rolls {}.".format(dice_sum))
# roll2dice()

# function name : player_bet
# arguments : bank - player money
# returns : the bet of the player
def player_bet(bank): 
    bet = input ("How much would you like to bet")