def maximun(l):
    max_temp = None
    for x in l:
        if not max_temp:
            max_temp = x
        else:
            max_temp = max(max_temp,x)
    return max_temp


def max_2(l):
    if len(l) == 0:
        return None
    if len(l) == 1:
        return l[0]
    first = l[0]
    rest = l[1:]

    maximum_of_rest = max_2(rest)
    
    return max(first, maximum_of_rest)


def quick_sort(l):
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l

    median_index = len(l)/2
    median = l[median_index]

    minors = []
    majors = []

    for x in range(0,len(l)):
        if x == median_index:
            continue
        
        if l[x] <= median:
            minors.append(l[x])
        else:
            majors.append(l[x])

    return quick_sort(minors) + [median] + quick_sort(majors)

print(quick_sort([9,7,8,2, -5, 6,9,10,17,2,1]))