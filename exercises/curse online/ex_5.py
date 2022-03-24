
number_1 = int(input("Give me the first number: "))
number_2 = int(input("Give me the second number: "))

if number_1 < number_2:
    inter_num = []
    for n in range(number_1, (number_2 + 1)):
        inter_num.append(str(n))
        print(",".join(inter_num))

else: 
    print("The number 1 must be lower than number 2 ")