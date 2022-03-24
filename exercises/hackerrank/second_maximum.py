
# sacar el segundo maximo de un diccionario

# def second_max(l):
#     count_dict = count(l)

#     first_max_key = max_dict(count_dict)
#     del count_dict[first_max_key]
#     return max_dict(count_dict)

# def count(l):
#     d = {}
#     for x in l:
#         if not d.get(x, None):
#             d[x] = 0
#         d[x] += 1
#     return d

# def max_dict(d):
#     max_temp_key = None
#     max_temp_value = None

#     for key in d.keys():
#         if not max_temp_value or max_temp_value < d[key]:
#             max_temp_key = key
#             max_temp_value = d[key]
        
#     return max_temp_key

#print(second_max([4,4,8,3,2,2,2,1]))





def count(l):
    d = {}
    for x in l:
        if not x in d:
            d[x] = 0
        d[x] += 1
    return d


def max_in_dict(d):
    max_temp_d_key = None
    max_temp_d_value = None
    for key in d.keys():
        if d[key] > max_temp_d_value:
            max_temp_d_key = key 
            max_temp_d_value = d[key]
    return max_temp_d_key


def second_max(l):
    count_dic = count(l)
    print(count_dic)

    max_number = max_in_dict(count_dic)
    del count_dic[max_number]
    return max_in_dict(count_dic)

print(second_max([2,4,5,3,2,1,5,5,7,7,8]))
        



