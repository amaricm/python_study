import random

def diff_set(a, b):
    d_b = {}
    result = []
    for i in b:
        d_b[i]= "num"
    for y in a:
        if not  d_b.get(y) and not y in result:
            result.append(y)

    return result


def diff_set_no_dict(a,b):

    result = []

    for x in a:
        exists = False
        for y in b:
            if x == y:
                exists = True
                break
        if not exists:
            result.append(x)
    
    return result

#a1 = [2, 1, 4, 5, 8]
#b1 = [4, 2, 1, 6, 9]

a1 = []
b1 = []

for x in range(0,10**6):
    a1.append(random.randint(0,100))
    b1.append(random.randint(0,50))

print("Dictionary solution")
print(diff_set(a1, b1))


        