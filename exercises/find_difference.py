def find_difference_set(l,p):
    dict_p = {}
    result = []
    for i in p:
        dict_p[i]= "num"
    for t in l:
        if not dict_p.get(t, False):
            result.append(t)
    return result 

l1 = [3, 4, 5, 2, 1]
p2 = [8, 4, 2, 1]    
print(find_difference_set(l1, p2))
            