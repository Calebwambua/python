class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_name(self):
        print(f"My name is{self.first_name},{self.last_name},and im {self.age} years old")

class Student(Person):
    def __init__(self,first_name,last_name,age):

        super().__init__(first_name,last_name,age)
my_student = Student(first_name="John",last_name="Smith",age=25)
my_student.print_name()
my_student2 = Student(first_name="Jackton",last_name="Mboya",age=24)
my_student2.print_name()
my_student3 = Student(first_name="Jason",last_name="Smith",age=21)
my_student3.print_name()
my_student4 = Student(first_name="Jorga",last_name="Smith",age=22)
my_student4.print_name()
my_student5 = Student(first_name="will",last_name="Smith",age=23)
my_student5.print_name()