import random

def duplicate_key_no_dict(l):
    duplicates = []
    for x in range(0,len(l)):
        for y in range(x,len(l)):
            if l[x] == l[y]:
                duplicates.append(l[x])
    return duplicates


def duplicate_key_dict(l):
    m = []
    d = {}
   
    for i in l:
        if not d.get(i, False):
            d[i] = 1
        else:
            d[i] = d[i] + 1
    
    for key in d.keys():
        if d[key] > 1:
            m.append(key)

    return m
    

l2 = []
for i in range(0,10**6):
    l2.append(random.randint(0,100))

print(duplicate_key_dict(l2))