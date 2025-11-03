class Student:
    def __init__(self, rollno, name, course):
        self.rollno = rollno
        self.name = name
        self.course = course
    def displayStudent(self):
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Course:", self.course)
stud1 = Student(4, "Ram", "MCA")
stud2 = Student(6, "Aiswarya", "MCA")
stud1.displayStudent()
stud2.displayStudent()
