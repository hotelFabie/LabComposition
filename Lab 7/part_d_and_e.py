#The E part seems to complement/extend part D, so they are within the same one.

#Part D 

#1

#2

#3

#4

#5

#6

#Part E

#1
class Teacher:
    def __init__(self, name : str):
        self.name = name

#2
class Course:
    def __init__(self, name : str, teacher : Teacher, students : list[Student] = []):
        self.name = name
        self.teacher = teacher
        self.students = students

    #6 (Method part)
    def add_student(self, student):
        self.students.append(student)

#3
teacher = Teacher("Anne")
course = Course("Discrete Mathematics", teacher)

#4
print(f"Course name: {course.name}")
print(f"Course teacher's name: {course.teacher.name}")

#6 (Student adding part)
course.add_student(Student())
course.add_student(Student())
course.add_student(Student())
#gonna fix this when I move back to part D.

#7
print("ALL STUDENT NAMES")
for student in course.students:
    print(student.name)

