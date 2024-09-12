## One object is associated with exactly one other object 
## passport / person 
class Passport:
    def __init__(self, number_pass):
        self.number_pass = number_pass
        
class Person:
    def __init__(self, name, passport):
        # validate passport is actually an object : isInstance()
        self.name = name
        self.passport = passport # One to One 
        
    def display(self):
        print(f"{self.name} has passport number {self.passport.number_pass}")


passport = Passport("487384A")
person = Person("Joseph", passport)

person.display()

##one to many: one object gets associated with multiple objects 
# Book and Authors : an author can write many books, but each book is written by only one author 
class Book:
    def __init__(self, title):
        self.title = title
        
class Author:
    def __init__(self,name):
        self.name = name 
        self.books = [] # aggregation : one to many relationship 
        
    def add_book(self,book):
        self.books.append(book)
        
    def list_book(self):
        print(f'{self.name} has written the following books')
        for book in self.books:
            print(f'- {book.title}')
            
author = Author("JK Rowling")
book1 = Book("Harry Potter and the philospher stone")
book2 = Book("Harry Potter and the chamber of secrets")


author.add_book(book1)
author.add_book(book2)

author.list_book()

## Many to many : multiple objects on both sides of the relationship can be associated to multiple on the other side 
## students and courses : a student can enroll in many courses and each course can have many students 

class Student:
    def __init__(self,name):
        self.name = name 
        self.courses = [] # many to many : aggregation on both sides 
        
    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)
        
class Course:
    def __init__(self,title):
        self.title = title
        self.students = [] #many to many : aggregation on both sides 
        
    def list_students(self):
        print(f"Students enrolled in {self.title}")
        for student in self.students:
            print(f'- {student.name}')
            

student1 = Student('Joseph')
student2 = Student('Jabez')
course1 = Course('Software Engineering')
course2 = Course('Data Science')

student1.enroll(course1)
student1.enroll(course2)
student2.enroll(course1)

course1.list_students()
course2.list_students()

