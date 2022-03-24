def count_keys(a):
    count = 0
    for i in a.keys():
        count = count + 1
    return count

a1 = {'a':2, 'b':4, 'c':5}
print(count_keys(a1))


def find_number(b,c):
    for y in b.keys():
        if c == y:
            return True
    
    print("Yo solo llego aqui si es False")
    return False

a1 = {'a':2, 'b':4, 'c':5}
print(find_number({'a':2, 'b':4, 'c':5}, 'b'))



