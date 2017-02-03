import random
# function name: scramble_word
#   purpose: To scramble the letters in the middle of a word besides the first and the last
#   arguments: victim - the word that is being scrambled
#   returns: scrambled word
#-------------------------------------- SUDO CODE --------------------------------------
# 1st - You print the regular word
# 2nd - You find out if the regular word has more than 3 letters
# 3rd - If it doesn't, tell the user in put in a different word
# 4th - If it does, then turn the word given into a list
# 5th - When the word becomes a list, keep the first and last index the same
# 6th - Rearange the index's inside of the word, the ones before the last index and the ones after the first index
# 7th - Turn it back into a string
# 8th - Print the new word
def scramble_word(victim):
    if len(victim) > 3:
        victim = list(victim)
        random.shuffle(victim[1:-1])
        print (victim)

scramble_word('letter')