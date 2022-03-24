class Classroom(object):
    board_number = 1

    def __init__(self, class_name, chair_number, table_number, board, students):
        """
        #comment
        student type: list[Student]
        """
        self.class_name = class_name
        self.chair_number = chair_number
        self.table_number = table_number
        self.students = students
        self.teacher_list = []
        self.board = board
    
    def  fire_student_by_name(self, name):
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                return
    def fire_student(self, student):
        self.students.remove(student)

    def fire_older_than(self, age):
        for student in self.students:
            if student.age > age:
                self.students.remove(student)
    
    def failed_in(self, asignature):
        failed_list = []
        for student in self.students:
            if student.has_failed(self, asignature):
                failed_list.add(student.name)
        return failed_list

class Student(object):
    def __int__(self, name, age, list_of_notes):
        self.list_of_notes = list_of_notes
        self.name = name
        self.age = age

    def has_failed(self, asignature):
        for note in self.list_of_notes:
            if note.asignature == asignature:
                return note.value < 3
            



class Note(object):
    def __int__(self, asignature, value):
        if value < 0 :
            raise Exception("notes have to have a value higher than 0")
        self.asignature = asignature
        self.value = value


class Teacher(object):
    def __int__(self, name, age)
        self.name = name
        self.age = age