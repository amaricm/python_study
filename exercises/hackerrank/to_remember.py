def exist(element, list):
    for a in list:
        if element == a:
            return True
    return False

def maximun(l):
    max_temp = None
    for x in l:
        if not max_temp:
            max_temp = x
        else:
            max_temp = max(max_temp,x)

def count(l):
    d = {}
    for x in l:
        if not x in d:
            d[x] = 0
        d[x] += 1
    return d
print(count([3, 4, 4, 5,  4, 3, 2, 1, 1]))