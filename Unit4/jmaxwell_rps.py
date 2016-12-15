import random
#function name: get_p1_move
#   arguments: none
#   purpose: present player with options, use input() to get player move
#   returns: the player's move as either 'r', 'p', or 's'
def get_p1_move():
    x = input("\n1 = Rock👊\n2 = Paper💸\n3 = Scissors🔪 \nEnter a Number from 1-3: ")
    if x == "1":
        return 'r'
    elif x == "2":
        return 'p'
    elif x == "3":
        return 's'

#function name: get_comp_move():
#   arguments: none
#   purpose: randomly generates the computer's move,
#            either 'r' 'p' or 's'
#   returns: the computer's randomly generated move
def get_comp_move():
    comp_move = random.randint(1,3)
    if comp_move == 1:
        return 'r'
    elif comp_move == 2:
        return 'p'
    elif comp_move == 3:
        return 's'

#function name: get_rounds
#   arguments: none
#   purpose: allows the user to choose a number of rounds from 1 to 9.
#   returns: the user-chosen number of rounds
def get_rounds():
    number_of_rounds = input("How many rounds would you like to play💯😇? ")
    return int(number_of_rounds)
#function name: get_round_winner
#   arguments: player move, computer move
#   purpose: based on the player and computer's move, determine
#            the winner or if it's a tie
#   returns: returns a string based on the following:
#               "player" if player won
#               "comp" if computer won
#               "tie" if it's a tie
def get_round_winner(p1move, cmove):
    if p1move == 'r' and cmove == 's':
        print ("\n🔪The Computer selected Scissors🔪")
        print ("\n👊You Selected Rock👊")
        return "\nPlayer 1 Wins the Round \n"
    elif p1move == 'p' and cmove == 'r':
        print ("\n👊The Computer selected Rock👊")
        print ("\n💸You Selected Paper💸")
        return "\nPlayer 1 Wins the Round \n"
    elif p1move == 's' and cmove == 'p':
        print ("\n💸The Computer selected Paper💸")
        print ("\n🔪You Selected Scissors🔪")
        return "\nPlayer 1 Wins the Round \n"
    elif p1move == 's' and cmove == 'r':
        print ("\n👊The Computer selected Rock👊")
        print ("\n🔪 You Selected Scissors🔪︎")
        return "\nComputer Wins the Round \n"
    elif p1move == 'r' and cmove == 'p':
        print ("\n💸The Computer selected Paper💸")
        print ("\n👊You Selected Rock👊")
        return "\nComputer Wins the Round \n"
    elif p1move == 'p' and cmove == 's':
        print ("\n🔪 The Computer selected Scissors🔪︎")
        print ("\n 💸You Selected Paper💸")
        return "\nComputer Wins the Round \n"
    elif p1move == 'r' and cmove == 'r':
        print ("👊You both selected Rock👊")
        return "\nThis Round Was a Tie \n"
    elif p1move == 's' and cmove == 's':
        print ("🔪You both selected Scissors🔪︎")
        return "\nThis Round Was a Tie \n"
    elif p1move == 'p' and cmove == 'p':
        print ("💸You both selected Paper💸")
        return "\nThis Round Was a Tie \n"
    
    

#function name: get_full_move
#   arguments: a single letter move 'r','p', or 's'
#   purpose: returns the "full" word of a given move
#   returns: returns a string based on the following:
#               "Rock" if given "r"
#               "Paper" if given "p"
#               "Scissors" if given "s"
def get_full_move(shortmove):
    if shortmove == 'r':
        return "Rock"
    elif shortmove == 's':
        return "Scissors"
    elif shortmove == 'p':
        return "Paper"

#function name: print_score
#   arguments: player score, computer score, number of ties
#   purpose: prints the scoreboard
#   returns: none
def print_score(pscore, cscore, tie):
    print ("You have {} points \nThe computer has {} points\nYou guys tied {} times.".format(pscore,cscore, tie))
    pscore = int(pscore)
    cscore = int(cscore)
    tie = int(tie)

# function name: rps
#   arguments: none
#   purpose: the main game loop.  This should be the longest, using
#               all the other functions to create RPS
# #   returns: none
def rps():
    player_score = 0
    comp_score = 0
    ties = 0
    rounds = get_rounds()
    for x in range(rounds):
        player_1 = get_p1_move()
        computer_1 = get_comp_move()
        winner = get_round_winner(player_1,computer_1)
        print(winner)
        if winner == "\nPlayer 1 Wins the Round \n":
            player_score = player_score + 1
        elif winner == "\nComputer Wins the Round \n":
            comp_score = comp_score + 1
        elif winner == "\nThis Round Was a Tie \n":
            ties = ties + 1
        print_score(player_score, comp_score, ties)
        
        if player_score > rounds / 2:
            break
        elif comp_score > rounds / 2:
            break
    
    if player_score > comp_score:
        print ("\nYOU WIN WITH {} POINTS💯👋😍👌".format(player_score))
    elif comp_score > player_score:
        if comp_score - player_score == 1:
            print ("\nYOU LOSS BY {} POINT!!!😡😓😱😳".format(comp_score - player_score))
        elif comp_score - player_score > 1:
            print ("\nYOU LOSS BY {} POINTS!!!😡😓😱😳".format(comp_score - player_score))
    elif comp_score == player_score:
        print ("\nYOU TIED WITH THE COMPUTER!!!😈😔😁😂")
    
        
rps()