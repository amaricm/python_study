def winner_list(a, b):
    win_list = [0,0]
    for t in range(0, len(a)):
        if a[t] >b[t]:
            win_list[0] += 1
        else:
            win_list[1] += 1
    return win_list
print(winner_list([2, 5, 9], [36, 1, 99]))






    # if a[0] > b [0]:
    #     win_list[0] += 1
    # else:
    #      win_list[1] += 1
