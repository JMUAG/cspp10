def swap(values,index1,index2):
    for x in range(len(values)):
        if values[x] == index1:
            values[x] = index2
        elif values[x] == index2:
            values[x] = index1
        
values = [1,2,3,4,5,6]
swap(values,[2],[5])
print (values)