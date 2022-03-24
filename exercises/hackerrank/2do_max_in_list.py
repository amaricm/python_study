

# def dic_count(list1):
#     count = {}
#     for b in list1:
#         if not count.get(b, None):
#             count[b] = 0
#         count[b] += 1
#     return count
# print(dic_count([2,3,2,3,4,5,3,2,2,2,]))        


def maximun(l):
    max_temp = None
    for x in l:
        if not max_temp:
            max_temp = x
        else:
            max_temp = max(max_temp,x)


def sort_count(count):
 




