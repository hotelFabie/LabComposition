#Part F

class Student:
    def __init__(self, name : str, score : int):
        self.name = name
        self.score = score

        def get_status(self):
            if self.score >= 70:
                return "PASS"
            else:
                return "FAIL"

class Teacher:
    def __init__(self, name : str):
        self.name = name

class Course:
    def __init__(self, name : str, teacher : Teacher, students : list[Student]):
        self.name = name
        self.teacher = teacher
        self.students = []
    
    def get_passing_students(self):
        #raise ValueError -- maybe that we raise an error here.

        passing_students = []
        for student in self.students:
            if student.get_status() == "PASS":
                passing_students.append(student)
        return passing_students

#9: Five Student objects, one Teacher object, one Course object

#10: Summary print