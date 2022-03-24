def sum_list(l):
    for i in range(0,len(l)):
        if i == 0:
            continue
        print(l[i] + l[i-1])
    return sum

l2 = [2, 5, 7, 8,6]
sum_list(l2)