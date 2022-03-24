number_1 = int(input("Give me the first number: "))
number_2 = int(input("Give me the second number: "))

min_number = min(number_1, number_2)
max_number = max(number_1, number_2)

for n in range(min_number, max_number + 1):
    if n % 2 == 1:
        print(n)


