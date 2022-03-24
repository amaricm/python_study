

# n = 1 
# mult = [] 
# if n > 11:  
#     break
# for y in range(1, 11):        
#     mult = n * y 
#     n += 1
# print(f"Multiplication Table of {n}")
# print(f" {n} * {y} = {mult}")

n = 1 
while n < 10:
    print(f"Multiplication Table of {n}")
    for y in range(1, 11):        
        mult = n * y         
        print(f" {n} * {y} = {mult}") 
    n += 1     
        
