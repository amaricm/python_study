
def swap(l, pos1, pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp


def reverse_word(s):
    l = list(s)
    start = 0
    end = len(s) - 1
    
    while start < end:
        swap(l, start, end)
        start += 1
        end -= 1

    name = ""
    for x in l:   
        name = name + x
    return name 

    
print(reverse_word("amarilis"))


