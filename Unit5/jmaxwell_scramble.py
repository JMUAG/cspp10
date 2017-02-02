import random

# function name: scramble_word
#   purpose: To scramble the letters in the middle of a word besides the first and the last
#   arguments: victim - the word that is being scrambled
#   returns: scrambled word

# 1st - You print the regular word
# 2nd - You find out if the regular word has more than 3 letters
# 3rd - If it doesn't, tell the user in put in a different word
# 4th - If it does, then turn the 
def scramble_word(victim):
    print(victim)
    if len(victim) > 3:
        victim = list(victim)
        random.shuffle(victim)
        print (victim)

scramble_word('letter')