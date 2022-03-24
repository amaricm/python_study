

student_name  = 0
student_note  = 0

approved = []
failed = []
count = 0 
while count < 3:
    student_name  = input("Give me the name of the student: ")
    student_note  = int(input("Give me the note  of the student: "))
    if student_note >= 3:
        approved.append( (student_name, student_note) )
    else:
        failed.append( (student_name, student_note) )
    count +=1
print(f" the amount of the aproved are {len(approved)}" )
print(f" the amount of the failed are {len(failed)}" )





# note_list = []
# count = 0 

# for n in range(1, 16):
#     note_list.append(student_name, student_note)
#         if student_note < 3:
#             count +=1
# print(count)





