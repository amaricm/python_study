
def fibonacci(n):
    if n < 0: 
        raise Exception("Possitive number is required") 
    if n == 1 or n == 2:
        return 1
    
    fib_1 = 1
    fib_2 = 1

    for _ in range(0, n):
        temp = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = temp

    return fib_2

print(fibonacci(3))