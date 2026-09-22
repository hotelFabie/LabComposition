#The E part seems to complement/extend part D, so they are within the same one.

#Part D 

#Assuming that we add the class to even begin with.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #4
    def get_status(self):
        if self.score >= 80:
            return "PASS"
        return "FAIL"

#1
s1 = Student("John", 60)
s2 = Student("Martin", 95)
s3 = Student("Xavier", 85)
s4 = Student("Jessica", 40)
s5 = Student("Tanya", 99)
s6 = Student("Faily", 0)

#2
students = [s1, s2, s3, s4, s5, s6]

#3
for index, student in enumerate(students, start=1):
    print(f"[{index}] {student.name} - {student.score}")

#5
for student in students:
    print(f"{student.name}: {student.get_status()}")

#6
at_least_70_score_students = [student for student in students if student.score >= 70]
#Proof by printing attributes; no point in printing just the object and getting no human language value from it.
for student in at_least_70_score_students:
    print(f"{student.name} - {student.score}")

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
course.add_student(Student("Jeremiah", 70))
course.add_student(Student("Ishamel", 90))
course.add_student(Student("Jacques", 95))

#7
print("ALL STUDENT NAMES")
for student in course.students:
    print(student.name)

