from pprint import pprint

program = {
    
}

def add(program):
    add_user = input("What would you like to be your key? ").lower()
    if add_user not in program:
        add_user2 = input("What would you like to be your value? ").lower()
        program[add_user] = add_user2
    

def remove(program):
        remove_user = input("What would you like to remove? ").lower()
        if remove_user in program:
            del program[remove_user]
            
def update(program):
    update_user = input("Which Key would you like to modify? ").lower()
    if update_user in program:
        update_key = input("What is the new key? ").lower()
        update_value = input("What is the new value? ").lower()
        program[update_key] = update_value
        
def print_dic(program):
    pprint(program)
    
def main(program):
    choice = "djndsd"
    while choice != "exit":
        user_input = input("Would you like to | Add | Remove | Update | Print | Exit | ").lower()
        if user_input == "add":
            add(program)
        elif user_input == "remove":
            remove(program)
        elif user_input == "update":
            update(program)
        elif user_input == "print":
            print_dic(program)
        elif user_input == "exit":
            print("You will now be gone!")    
            break
        
main(program)        