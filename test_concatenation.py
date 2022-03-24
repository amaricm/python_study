import time

counter = "0"
i = 0

# start = time.time()
# while i < 10**6:
#     counter = counter + "," + str(i)
#     i = i + 1
# end = time.time()

# #print(counter)
# print(f"Elapsed Time with Concatenation: {end - start}")


start2 = time.time()
list = []
for numbers in range(1, 10**6):
    list.append(str(numbers))
final = " , ".join(list)
end2 = time.time()

print(f"Elapsed Time with Join: {end2 - start2}")
