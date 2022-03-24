
def exist(element, list):
    for a in list:
        if element == a:
            return True
    return False

def exists_in_l1_but_not_l2(l1, l2):
    diff_set = []
    for a in l1:
        if exist(a, l2):
            continue
        diff_set.append(a)
    return diff_set

l1 = [1,2,5]
l2 = [1,3,5]

diff_set = exists_in_l1_but_not_l2(l1,l2) + exists_in_l1_but_not_l2(l2,l1)

print(diff_set)


# def no_duplicate_in_list(list_1, list_2):
#     new_list = []

  
#   for a in list_1:
#         for b in list_2:
#             if a != b:
#                 new_list.append(a)
#                 break
#             else:
#                 break

#     return new_list
# print(no_duplicate_in_list([1,1, 2, 3, 4], [4, 5, 2, 3, 5, 9]))







#     # for a in list_1:
#     #     if a not in list_2 and a not in new_list:
#     #         new_list.append(a)
#     # for b in list_2:
#     #     if b not in list_1 and b not in new_list:
#     #         new_list.append(b)
        

    








   
    
        
