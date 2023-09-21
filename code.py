class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, final_year_project):
        super().__init__(name, age, student_id)
        self.final_year_project = final_year_project
person1 = Person("Jospeh", 10)
student1 = Student("David", 100, "12345")
grad_student1 = GraduateStudent("Saleem", 10, "67890", "python Project")
print(person1.name, person1.age)
print(student1.name, student1.age, student1.student_id)
print(grad_student1.name, grad_student1.age, grad_student1.student_id, grad_student1.final_year_project)
