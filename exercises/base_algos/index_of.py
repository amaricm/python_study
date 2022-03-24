def index_of(l, elem):
    """
        returns index of element in list, 
        if not found return -1
    """
  
    for a in range(0, len(l)):  
        if l[a] == elem:
            return a
    return -1    
        

print(index_of([3,4,5,6], 7)) 


            
         
