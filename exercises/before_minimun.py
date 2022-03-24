def min_func(a):
    if len(a) == 0:
        return None
    elif len(a) == 1:
        return a[0]
    
    min_temporal = a[0]
    for i in a:
        if i < min_temporal:
            min_temporal = i
    
    return min_temporal

print(min_func([5,9,3]))
