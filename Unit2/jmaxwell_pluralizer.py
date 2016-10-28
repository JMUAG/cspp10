pluralizer = input("Enter a number: ")
pluralizer_2 = input("Enter a word that is not plural: ")
knife_change = "ves"
family_change = "ies"
bush_change = "es"
cactus_change = "i"
guy_change = "s"
regular_input = pluralizer_2

if pluralizer == "1" :
    print (pluralizer + " " + regular_input)
else:    
    if pluralizer_2[-2:] == "fe":
        print (pluralizer + " " + pluralizer_2[:-2] + knife_change)
    elif pluralizer_2[-2:] == "sh" or pluralizer_2[-2:] == "ch":
        print (pluralizer + " " + pluralizer_2 + bush_change)
    elif pluralizer_2[-2:] == "us":
        print (pluralizer + " " + pluralizer_2[:-2] + cactus_change)
    elif pluralizer_2[-2:] == "ay" or pluralizer_2[-2:] == "ey" or pluralizer_2[-2:] == "oy" or pluralizer_2[-2:] == "uy" or pluralizer_2[-1:] == "g":
        print (pluralizer + " " + pluralizer_2 + guy_change)
    elif pluralizer_2[-1:] == "y" and pluralizer_2[-2:] != "ay" or pluralizer_2[-2:] != "ey" or pluralizer_2[-2:] != "oy" or pluralizer_2[-2:] != "uy" or pluralizer_2[-1:] != "g":
        print (pluralizer + " " + pluralizer_2[:-1] + family_change)
    else: 
        print (pluralizer + " " + pluralizer_2 + guy_change)
    
    