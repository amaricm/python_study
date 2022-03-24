def permutation(a,b):
    if len(a) != len(b):
        return False
    dic1 = {}
    dic2 = {}
    for i in a:
        if not dic1.get(i):
            dic1[i] = 0
        dic1[i] = dic1[i] + 1
    for y in b:
        if dic2.get(y):
            dic2[y] = dic2[y] + 1
        else:
            dic2[y] = 1

    for key in dic1.keys():
        if not dic2.get(key) or  dic1[key] != dic2[key]:
            return False
    return True

a = "dayana"
b = "anadar"
print(permutation(a, b))