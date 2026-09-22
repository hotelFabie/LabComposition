#Part F

#1

#2
class Student:
    def __init__(self, name : str, score : int):
        self.name = name
        self.score = score

    #3
    def get_passing(self) -> str:
        #8
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

#4
class Teacher:
    def __init__(self, name : str):
        self.name = name

#5
class Course:
    def __init__(self, name : str, teacher : Teacher, students : list[Student] = []):
        self.name = name
        self.teacher = teacher
        self.students = students

    #6
    def add_student(self, new_student : Student) -> None:
        if new_student.score < 0:
            raise ValueError("Given score is under 0, which should not be possible.")
        
        self.students.append(new_student)

    #6
    def count_students(self) -> int :
        return len(self.students)

    #7
    def get_passing_students(self) -> list[Student]:

        passing_students = []
        for student in self.students:
            if student.get_passing() == "PASS":
                passing_students.append(student)
        return passing_students

#9
student1 = Student("Jüri", 50)
student2 = Student("Mawa", 65)
student3 = Student("Perkka", 90)
student4 = Student("Kasane", 99)
student5 = Student("Strangey", -5)

teacher = Teacher("Marissa")

course = Course("OOP", "Robotzi", [student1, student2, student3, student4])

#Will give a ValueError
#course.add_student(student5)

#Will work fine
student6 = Student("Excellenzi", 100)
course.add_student(student6)

print(course.count_students())

print(course.get_passing_students())

print(course.students[1].get_passing())
print(course.students[2].get_passing())

#10: Summary print