# # ex : parametres in function 

# # print("##### example 1  ####")

# # def show_your_name(name, age):
# #     print(f"Your name is : {name}")

# #     if age >= 18:
# #         print("You are an adult")

# # name  = input("Introduce your name: ")
# # age  = int(input("Introduce your age: "))
# # show_your_name(name, age)


# print("##### example 2  ####")

# def mult_function(my_number):  
#     print("result")
#     for a in range(1, 11):
#         result = my_number*a
#         print(f" {my_number} x {a} = {result}")
# my_number = int(input("Give me  number: "))
# mult_function(my_number)

# # si queremos hacer todas las tablas de pultiplicar , hacemos un ciclo para esta funcion 
# # queraria asi, habria que quitarle el input de arriba 
# for table_num in range(1, 11):
#     mult_funtion(table_num)

# print("##### example 3  ####")   
# #  return examples 

# def say_hello(name):
#     welcome = f"Hello my friend {name}"

#     return welcome

# print(say_hello("amarilis"))

print("##### example 4  ####")  

def sum(a,b):
    return a+b 

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b 

def div(a,b):
    return a/b 
 

def calculator_summary(number_1, number_2, basic=False):

    return f"""
        sum: {sum(number_1,number_2)}
        sub: {sub(number_1,number_2)}
        mult: {mult(number_1,number_2)}
        div: {div(number_1,number_2)}
    """
print(calculator_summary(3, 6)) 