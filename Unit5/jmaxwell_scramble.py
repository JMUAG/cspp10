import random

# function name: scramble_word
#   purpose: To scramble the letters in the middle of a word besides the first and the last
#   arguments: victim - the word that is being scrambled
#   returns: scrambled word

def scramble_word(victim):
    print(victim)
    if len(victim) > 3:
        victim = list(victim)
        random.shuffle(victim)
        print (victim)

scramble_word('letter')