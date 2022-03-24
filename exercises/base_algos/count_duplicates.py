def count(l):
    d = {}
    for x in l:
        if not x in d:
            d[x] = 0
        d[x] += 1
    return d
print(count([3, 4, 4, 5,  4, 3, 2, 1, 1]))