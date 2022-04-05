

# def kids_go_to_park(l):
#     for kid in l:
#         if kid.startswith("A"):
#             yield kid
    

# for kid in kids_go_to_park(["Jose", "Antonio", "Antonella", "Julieta"]):
#     print(kid)


# print(list(range(1,10)))


# def even_number(x):
#     l = []
#     for i in range(0, x):
#         if i % 2 == 0:
#             l.append(i)
#     return l 
# print(even_number(10))

def even_number(x):

    for i in range(0, x):
        if i % 2 == 0:
            yield i 
count = 1        
for even in even_number(100):
    if count > 2:
        break 
    count +=1
    print(even)
        
