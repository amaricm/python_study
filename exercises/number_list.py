def number_rep(l,a):
    rep_list = []
    for i in l:
        if a == i:
            rep_list.append(i)
    return rep_list

l2 = [2, 3, 5, 6, 3, 3]
print(number_rep(l2,2))
