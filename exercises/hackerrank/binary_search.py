

l = list(range(1,3*10**9))

#print(l)

def exist(a, l1):
    count = 0
    for x in l1:
        count += 1
        if x == a:
            print(count)
            return True 
    print(count)
    return False

def exist(a, t):
    for x in t:
        for c in x:
            if c == a:
                return True 
    return False




exist_var = exist("a", l)
print(exist_var)
