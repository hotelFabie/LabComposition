#Part D

#1
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee: {self.name}"

#2
class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def reflect(self):
        return f"Hmm..."

#3
class Engineer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def discuss():
        return "So if we do like this..."

#4
developer = Developer("Zeppi")
engineer = Engineer("Maku")

print(developer.get_information())
print(engineer.get_information())

#5
employee = Employee("Jake")
employee.reflect()
employee.discuss()
#First of all, the IDE already suggests it by no color indication, but it can not see everything that is based on it,
#rather the opposite: What is based on it can see what Employee consists of.  