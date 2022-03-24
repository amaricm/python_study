# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.




def minim_score(l):
    if len(l) == 0:
        return None
    min_temp = l[0]
    for i in l:
        if i[1] < min_temp[1]:
            min_temp = i
    return min_temp

def find_and_delete(l, item):
    new_list = []
    for student in l:
        if student[1] != item[1]:
            new_list.append(student)
    return new_list

def filter_equal(l, item):
    new_list = []
    for student in l:
        if student[1] == item[1]:
            new_list.append(student)
    return new_list    


# all_students = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         all_students.append([name, score])

all_students = [["rache", -50], ["Nawel", -50],["rosa", -50],["laura", 51]]
_min = minim_score(all_students)
print(_min)
clean_list = find_and_delete(all_students, _min)
print(clean_list)    
second_min = minim_score(clean_list)
print(second_min)
# result = filter_equal(clean_list, second_min)
     
# names = []
# for student in result:
#     names.append(student[0])
# names.sort()

# for sorted_name in names:
#     print(sorted_name)