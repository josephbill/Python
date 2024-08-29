# a dict comprehensions creates a new dict by applying an expression to key-value pairs from an iterable 
# {key_expression: value_expression for item in iterable if condition}

# mapping numbers to their squares 
# x : x**2

# squares_dict = {}
# for x in range(1,11):
#     squares_dict[x] = x ** 2
    
# print(squares_dict)
# dynamic programming : algorithm 
squares_dict = {x: x**2 for x in range(1,11)}
print(squares_dict)

students = [ ('Alice',85) , ('joseph', 70) ,('bob', 30) ]
# create a dict.that maps the students to their respective grades 
# {'alice': 85, ........}

def dictGrades(s):
    # mydict = {}
    return {name: grade for name,grade in s}
    # for student,grade in s:
    #     print(student,grade) 
    #     mydict[student] = grade
    # return mydict
    
print(dictGrades(students))