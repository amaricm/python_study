
def fibonacci(n):
    if n < 0: 
        raise Exception("Possitive number is required") 
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50)) 