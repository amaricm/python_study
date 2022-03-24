def indexof(string, character):
    for i in range(0, len(string)):
        if string[i] == character:
            return i
    return -1

def indexof_javi(string, character):
    index = 0
    for char in string:
        if char == character:
            return index
        index += 1
    return -1

def indexof_javi_while(string, character):
    i = 0
    while i < len(string):
        if string[i] == character:
            return i
        i += 1
    return -1    

print(indexof_javi_while("anto", "b"))