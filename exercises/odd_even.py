
#### en una lista poner pares adelante e impares atras####
def swap(l, left, right):
    var = l[left]
    l[left] = l[right]
    l[right] = var


def odd_even_possition(l):
   
    left = 0
    right = len(l) - 1

    while left < right:
        while l[left] % 2 == 0:
            left += 1
        
        while l[right] % 2 == 1:
            right -= 1

        swap(l, left, right)
        left += 1
        right -= 1

    return l
    
print(odd_even_possition([3, 8, 6, 9]))
