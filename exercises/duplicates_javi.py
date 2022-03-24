def duplicates_2(l):
    a = {}
    duplicates = []
    
    for x in l:
        a[x] = a.get(x,0) + 1

        if a[x] > 1 and not x in duplicates:
            duplicates.append(x)
    
    return duplicates

def duplicates(l):
    a = {}
    for x in l:
        a[x] = a.get(x,0) + 1
    
    duplicates = []
    for key in a.keys():
        if a[key] > 1:
            duplicates.append(key)
    
    return duplicates
    

l = [1,2,3,4,5,3,5,8,2]

print(duplicates_2(l))

# print "Input List: %s" %l 
# print("Duplicates: %s" % duplicates(l))