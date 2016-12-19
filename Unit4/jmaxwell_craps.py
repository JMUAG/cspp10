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
    print("Rolled 2 dice: {} and a {}\n".format(dice1,dice2))
    print ("This equals a {}".format(dice_sum))
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
        return roll_1 

# function name: second_roll_result
#   purpose: get the result of the second roll
#   arguments: roll_2 - the sum of the two dice rolled on second round
#   returns: the result of the second roll
def second_roll_result(roll_2,point):
    if roll_2 == 7:
        return "lose"
    elif roll_2 == point:
        return "win"
    else:
        return roll_2

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
            print ("That Is Not A Valid Bet Please Exit")
            break
        
# function name: bet_2
#   purpose: get the amount of money the player is betting after the first round of betting
#   arguments: cash_2 - the amount of money being bet the second time
#              bank_1 - the amount of money the player has
#   returns: The further of money the player is betting until they quit or loose
def bet_2(cash_2, bank_1):
    cash_2 = int(input("How Much Money Would You Like to Bet? "))
    while cash_2 <= bank_1:
        if cash_2 > bank_1:
            print ("That Is Not A Valid Bet Please Exit")
            break
        elif cash_2 <= bank_1:
            return cash_2
            
# function name: player_bank
#   purpose: show the amount of money the player has in the game
#   arguments: guapp - The amount of money the player has at the end of every round
#   returns: the amount of money the player has
def print_bank(guapp):
    print ("You have {} dollars left".format(guapp))

# function name: quit
#   purpose: to let the player quit the game when they don't want to play anymore
#   arguments: exit_key - The key on the key board that lets you exit
#   returns: either the end of the game or the continuation of the game
def quit(exit_key):
    exit_key = input("Would you like to continue [y|n]")
    exit_key = exit_key.lower()
    while exit_key == "y" or exit_key == "n":
        if exit_key == "n":
            break
        elif exit_key == "y":
            return "continue"
        else:
            print ("That is Invalid")
            
        
# function name: game_money
#   purpose: to increase your money 
#   arguments: round_result - The win or lose of a round
#              money_player - The amount of money the player has
#              bet - The amoount of money that was bet by the player
#   returns: the increase or decrease of your money
def game_money(round_result,money_player,bet):
    if round_result == "win":
        money_player = money_player + bet
    elif round_result == "lose":
        money_player = money_player - bet

# function name: craps
#   purpose: to form all the functions together to create the game
#   arguments:
#   returns: the game
def craps():
    print ("-------------WELCOME TO MY CASINO-------------\n")
    player_cash = amount_of_cash()
    point = 0
    win = 0
    first_bet = bet_1(player_cash)
    roll = roll2dice()
    result1 = first_roll_result(roll)
    result2 = second_roll_result(roll,point)
    print (first_bet)
    while player_cash >= 1:
        if result1 == "point":
            point = result1
        elif result1 == "win":
            player_cash = first_bet + player_cash
        elif result1 == "lose":
            player_cash = player_cash - first_bet
        elif result1 == "win":
            break
    print (player_cash)
                 
           
craps()