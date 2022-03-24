import time

def duplicates_ama(l):
    duplicate_list = []
    for i in range(0, len(l)): 
        if l[i] in duplicate_list:
            continue

        for j in range(i+1, len(l)):
            if l[j] == l[i]:
                duplicate_list.append(l[i])
                break
    return duplicate_list

def duplicates_javi(l):
    a = {}
    for x in l:
        if not a.get(x, None):
            a[x] = 0
        a[x] += 1
    
    duplicates_list = []
    for x in a.keys():
        if a[x] > 1:
            duplicates_list.append(x)

    return duplicates_list

import random

l = []
for x in range(1,10**8):
    l.append(1)

print("Empezamos a calcular")

start = time.time()
print(duplicates_ama(l))
end = time.time()
print(end - start)