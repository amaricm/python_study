# ## a list with 8 numbers 
# recorrer list and show it 
# hacer funcion que recoja lista de numeros y devuelva el string 
# order list and show it 
# mostrar longitud 
# show an element that user ask

### scroll and display the list###
# l = [2, 5, 4, 8, 5, 7, 3, 10]
# for a in l:
#     print(a)


### scroll and display the list and return an string###
# l = [2, 5, 4, 8, 5, 7, 3, 10]
# def covert_string(l):
#     result = ""
#     for a in l: 
#         result += " " + str(a) 
#     return(result)
# print(covert_string([2, 5, 4, 8, 5, 7, 3, 10]))


# order list and show it 
# def minimun(l):
#     if len(l) == 0:
#         return None
#     min_temp = l[0]
#     for num in l:
#         if num < min_temp:
#             min_temp = num
#     return min_temp

# def sort_list(l):
#     min_list = []
#     while len(l) > 0:
#         minimun_number = minimun(l)
#         min_list.append(minimun_number)
#         l.remove(minimun_number)
#     return min_list


# print(sort_list([2, 6, 2, 4, 7, 10]))

# def swap(l, pos_1, pos_2):
#     temp = l[pos_1]
#     l[pos_1] = l[pos_2]
#     l[pos_2] = temp
#     # return l
# # print(swap([3, 5, 6, 2, 3], 2, 3))

# def bubble_sort(l): 
#     action = True  
#     while action:  
#         action = False
#         for i in range(0, len(l) - 1):
#             if l[i] > l[i+1]:
#                 swap(l, i, i +1)
#                 action = True
       
#     return l
# # print(bubble_sort([3, 7, 1, 9, 7, 19, 8]))        



def insert_sort(l): 
    sorted = []
    for i in range(0, len(l)):
        added = False
        for j in range(0, len(sorted)):
            if sorted[j] > l[i]:
                added = True
                sorted.insert(j, l[i])
                break
        if not added:
            sorted.append(l[i])
    return sorted
print(insert_sort([3, 7, 1, 9, 7, 19, 8]))     



