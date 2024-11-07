class Student:
    
    class_year = 2024
    num_student = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("eric", 25)
student2 = Student("andy", 22)
student3 = Student("josh", 20)

print(student1.name, student1.age)
print(student2.name)
print(Student.class_year)
print(Student.num_student)