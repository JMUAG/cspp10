#Working With Johnson
def replace_all(original,to_replace,replace_with):
    for i in range(len(original)):
        if original[i] == to_replace:
            original[i] = replace_with
        
 
original = [1,2,1,3,5,1]
replace_all(original,1,"d")
print (original)