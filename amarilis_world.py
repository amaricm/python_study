input = "Julieta"
word_list = ["Julieta", "juama","torena","Julieta"]

for word in word_list:
    exists = True
    index = 0
    
    for letter in word:
        if letter != input[index]:
            exists = False
            break
        index = index + 1

    if exists:
        print("True")    
        

# for word in word_list:
#     exists = True
#     index = 0
#     for letter in word:
#         if letter != input[index]:
#             exits = False
#             break
#         index = index + 1
#     if exists:
#         print("True")

        