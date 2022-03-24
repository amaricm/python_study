# def even_odd(l):
#     new_l = []
#     for x in l:
#         if x%2 == 0:
#             new_l.insert(0, x)
#         else:
#             new_l.append(x)
#     return new_l

# def even_odd_2(l):
#     odd_list = []
#     even_list = []
#     for x in l:
#         if x%2 == 0:
#             even_list.append(x)
#         else:
#             odd_list.append(x)
#     return even_list + odd_list

def swap(l, pos1, pos2):
    temp = l[pos1]
    l[pos1] = l[pos2]
    l[pos2] = temp

def even_odd_in_place(l):    
    if not l:
        return

    start = 0
    back = len(l) - 1

    while start < back:
        while l[start] %2 == 0:
            start += 1

        while l[back] %2 == 1:
            back -= 1

        if start >= back:
            break

        swap(l, start, back)
    
    return l


print(even_odd_in_place([3, 4, 2, 5, 6, 9 , 5]))


