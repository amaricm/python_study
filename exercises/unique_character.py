def unique_character(w):
    dic_1 = {}
    for i in w:
        if dic_1.get(i):
           return False 
        dic_1[i] = " "
    return True


name = "x"

while name != "exit":
    print("Please Enter your name")
    name = input()
    print(f"Your name is unique: {unique_character(name)}")

