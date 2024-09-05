# association :: is a loose relationship btw two classes where one object uses another. 
# implies that objects can exist independently but can communicate when needed 

# example : Teacher and student 
class Teacher:
    def __init__(self,name):
        self.name = name 
        
    def teach(self, student):
        print(f"{self.name} is teaching {student.name}")
        
class Student:
    def __init__(self,name):
        self.name = name 
    
teacher = Teacher("Joseph Mbugua")
student = Student("Jabez Wekesa")

print(teacher.teach(student))