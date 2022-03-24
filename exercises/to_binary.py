import math

def to_binary(n):
    size = int(math.log(n,2))
    
    l =[]
    for i in range(size+1):
        l.append(0)

    while n > 0:
        b = int(math.log(n,2))
        l[size - b] = 1
        n = n - 2**b

    return l

def to_binary_recursive(n):
    print(n)
    if n == 0:
        return [0]

    b = int(math.log(n,2))
    next_log = int(math.log(n - 2**b, 2))
    print(next_log)
    mid_list = []
    for x in range(next_log, b):
        mid_list.append(0)

    return [1] + mid_list + to_binary_recursive(n - 2**b)

def get_decimal_form(n):
    size = int(math.log(n,10))
    
    l =[]
    for i in range(size+1):
        l.append(0)

    while n > 0:
        b = int(math.log(n,10))
        
        digit = int(n/(10**b)) 
        l[size - b] = digit
        n = n - 10**b*digit

    return l

print(to_binary(310))