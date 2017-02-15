from pprint import pprint

program = {
    
}

def add(program):
    ask_user = input("Would you like to add or remove to the dictionaries? ").lower()
    if ask_user == "add":
        add_user = input("What would you like to be your key? ")
        add_user2 = input("WHat would you like to be your value? ")
        program[add_user] = add_user2
        print(program[add_user])

add(program)
        
    # elif ask_user == "remove":
    #     remove_user = input("What would you like to remove?")
    #     if remove_user in program:
    #          program = {
                 
    #          }   