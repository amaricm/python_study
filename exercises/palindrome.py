def reverse(w):
    result = ""
    for x in w:
        result = x + result
    return result

def ____palindrome(w):
    return reverse(w) == w

def ___palindrome(p):
    print(p)
    if len(p) == 0 or len(p) == 1:
        return True 
    result = p[0] == p[len(p)-1] and palindrome(p[1:len(p)-1])

    print("Vengo virando")

    return result
        
def palindrome(p):
    first_index =0
    last_index = len(p)-1
    while first_index != last_index:
        if p[first_index] != p[last_index]:
            return False 
        first_index +=1 
        last_index -=1
    return True

print(palindrome("toataot"))

