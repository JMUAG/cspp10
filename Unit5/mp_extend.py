def extend(original,extension):
    for x in extension:
       original.append(x)
    
original = [1,2,3]
extension = [5,6,7]
extend(original,extension)
print (original)