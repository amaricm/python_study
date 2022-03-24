def my_list_function():
    return [1,2,3]

print("First time")
for i in range(1,4):
    print(i)

print("Second time")
for i in [1,2,3]:
    print(i)

print("Third time")
for i in my_list_function():
    print(i)