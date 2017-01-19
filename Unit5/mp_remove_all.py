#Working With Johnson
def remove_all(original,target):
    for i in range(original.count(target)):
        original.remove(target) 
        
original = [1,2,1,3,5,1]
remove_all(original,1)
print (original)