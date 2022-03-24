
def insert_order(l, elem):
    for i in range(0,len(l)):
        value = l[i]
        if elem < value:
            l.insert(i, elem)
            return l
    l.append(elem)  
    return l


# cuando en el for quiero terminar cuando algo se cumpla , pongo un return  
# para que no haga las proximas lineas que esta fuera del for, despues del return todo acaba 
# la otra opcion es crear una variable fuera del for y guardar un valor que despues pueda usar como el True o False 

def insert_sort(l):
    new_list = []
    for x in l:
        new_list = insert_order(new_list, x)
            
    return new_list 

print(insert_sort([3, 1, 2, 9]))



def order_per_elem(l, elem):
    for x in range(0, len(l)):
        if l[x] > elem:
            l.insert(x, elem)
            return l 
    l.append(elem)
    return l



def insert_sort(l):
    new_list = []
    for x in l:
        new_list = order_per_elem(l, x)
    return new_list

print(insert_sort([3,5,8,6,1])) 






















