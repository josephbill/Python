# is a 'has-a' relationship 
# implies a weak form of ownership where one object contains another , but both can exist 
# independently 

# school departments and teachers 
class Department:
    def __init__(self,name):
        self.name = name
        self.teachers = [] #aggregates multiple teacher objects 
        
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
        
    def list_teacher(self):
        for teacher in self.teachers:
            print(teacher.name)
            
class Teacher:
    def __init__(self,name):
        self.name = name 
        
dept = Department("Software Engineering")
teacher1 = Teacher("joseph mbugua")
teacher2 = Teacher("X mbugua")

dept.add_teacher(teacher1)
dept.add_teacher(teacher2)

print(dept.list_teacher())