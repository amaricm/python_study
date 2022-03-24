def sum_list(l):
    sum = 0
    for a in range(0, len(l)):
        sum = sum + l[a]
    return sum

print(sum_list([3, 4, 6]))

