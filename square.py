def square(number):
    return number**2

#print(square(5))

def rectangle_area(edge1, edge2):
   return edge1*edge2

edge1   = 3
edge2   = 4
area    = rectangle_area(edge1,edge2)

def pyarea(pyedge1,pyedge2,pyh):
    return rectangle_area(pyedge1,pyedge2) * pyh/3

pyedge1 = 4
pyedge2 = 6
pyh = 10

print(pyarea(pyedge1,pyedge2,pyh))

# print(f"Edge 1 = {edge1}")
# print(f"Edge 1 = {edge2}")
# print(f"Area is {area}")

