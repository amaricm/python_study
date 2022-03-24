
def my_function(a,b):
    try:
        a = int(a)
        b = int(b)

        c = a/b
        print(f"C is the result of division of {a}, {b}")
        print(f"C value is: {c}")
    except ZeroDivisionError:
        print("Mi hermano la division por cero no existe")
    except ValueError:
        print("Mi hermano como me vas a entrar letras")


while True:
    a = input("mi hermano entra un numero: ")
    b = input("entra el otro: ")

    my_function(a,b)