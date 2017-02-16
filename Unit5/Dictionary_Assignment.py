from pprint import pprint

program = {
    
}

def add(program):
    add_user = input("What would you like to be your key? ")
    add_user2 = input("What would you like to be your value? ")
    program[add_user] = add_user2
    

def remove(program):
        remove_user = input("What would you like to remove? ")
        if remove_user in program:
            del [remove_user]
            
def update(program):
    update_user = input("Which Key would you like to modify? ")
    if update_user in program:
        update_key = input("What is the new key? ")
        update_value = input("What is the new value? ")
        program[update_key] = update_value
        
add(program)

