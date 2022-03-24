def minimunnumber(l):
    if len(l) == 0: 
        return None
    elif len(l) == 1:
        return l[0]
       
    min_temporal = l[0]
    for a in l: 
        if a < min_temporal:
            min_temporal = a 
      
    return min_temporal  
print(minimunnumber([1, 4, 5, 9, 6, 2]))

