## Variables and Scoping 
- a symbolic name that references or points to an object in memory 
- container of information 

syntaxt 
variablename = "10"

## Scoping 
Scope refers to the region of a program where a particular variable is accessible 

- Local Scope 
- Enclosing Scope 
- Global Scope 
- Built in scope 


## PYTEST 
1. Install pytest : pip install pytest
2. Identify the units that you test , 1. File 2. Functions/ Procedures 
3. Create the test file : test_testapp.py
4. Inside the file import pytest and methods to test , define the testing methods 
def test_functionname():
    logic for testing 
5. After defining all logic head to terminal and run pytest 


### ipdb 
iPython Debugger : 
1. install ipdb using pip install ipdb 
2. Import the package in the file of use 
3. Insert a breakpoint in the code as per the debugging : When the code reaches that line it will pause the execution and open an interactive debugging session
4. Using ipdb in the command line by running this command 
python -m ipdb yourscript.py

Common Ipdb commands 
1. n : next : executes the current line and stops at the next line in the current function

2. s : step : step into the function called in the current line 
3. c : continue : continue the execution until the next break point 
4. p : print : evaluates and prints an expression 
5. l : lisst : displays the source code around the current line
6. b : breakpoint : sets a breakpoint at the specified line
7. q : quits : Quits the debuggers and stops the program

exit()  quits ipdb and refactors back to main shell

### TO Debug in python 
1. simple prints : prove that the values are there 
2. using pytest : TEST DRIVEN DEVELOPMENT 
3. ipdb : Interactive shell to investigate your function


## Data Structures
- A way of organizing and storing data efficiently in a computer program 
- Python several built in data structures 
1. Lists 
2. Tuples 
3. Dictionaries 
4. Sets 


### lists 
A list is an ordered, mutable collections of items 
Items can be of different data types 

variablename = [1,2,3,4,5,"Joseph", true]

### tuples 
A tuple is an ordered, immutable collection of items 

my_tuple = (10,20,"Joseph",true)

### Dictionary 
A dictionary is an unordered collection of key and value pairs. Keys are unique, and used to access values 
Dictionaries are mutable, meaning values can be updated and new key values can be added. 
my_dict = {
    "key1" : "value",
    "Key2" : {
        "Key1" : [
            1,2,3,5,
        ]
    }
}


### Sets 
A set is an unordered collection of UNIQUE ELEMENTS. Sets are useful when we need to ensure all elements are unique 

myset = {1,2,3,5,6} : literal notation
myset = set([1,2,3,4]) : set constructor

### Loops 
1. Executing a block a code repeatedly 

for loop : for ...  in  : used to iterate of a sequence (list, tuples, dictionaries , sets, Strings)
"String" : x.length  ["s","t","r" .... ]


, while loop : repeats as long as a condition true 


Looping data structures is simply the process of access and manipulating elements within collections like lists, tuples , dictionaries ,sets and strings 

for .... in 


## COMPUTATIONAL THINKING 
Logical approach to analysing a problem, produce a solution that can be understood by both humans and by computers

1. Abstraction : filtering out information that is not necessary to solve a problem 
2. Decomposition : Breaking down problems into sub problems , decomposition leads to modularity -> procedures (functions)
3. Data Modelling : Involves analysing and organising data. 
4. Pattern Recognition : Looking for patterns or common solutions to problems , data types and in built operations, searching and sorting 
5. Algorithmic thinking : Algorithm design (step by step process to output desired solution)


Sequences 
1. Assignments : variables 
2. Sequence : number of steps to be performed one after the other esp. on the assignment (1)
3. Selection : under certain conditions perform some steps , otherwise different or no steps.
4. Repetition : a sequence of steps performed a number of times 

https://gist.github.com/josephbill/a600b09026559760ad61fdf2973ba7c7


### Decorators 
A feature that allows modification or extension of behaviors of functions or methods 
Tasks : logging, access control , memoization

A decorator  is a FUNCTION that takes another function as an argument and returns a new function that usually extends the behaviour of the original function.  


### Comprehensions 
Comprehensions are a concise way to create sequences and collections 
- lists , dictionaries and sets
 
syntax for comprehensions 
[expressions for item in iterable if condition]


### OOP (Object Oriented Programming)
- a model(a way of writing code) that centers around OBJECTS( - is sth that has behaviours i.e. methods and attributes / data type : data structure that contains key/value pairs ) rather than functions

#### Key concepts 
1. CLASS : - a blueprint for creating objects : instructions on how to create the objects : 
2. OBJECTS : - an object is specific to a blueprint(class)
             - an instance of a class. 
             - an object has to have its own set of attributes and should be able to perform actions defined by the class.(behaviours)
3. Attributes : - the characteristics or properties of an object. These are variables which are associated with the object. 
4. Methods : - Functions defined within that class that describes the behaviours of our objects


## PILLARS OF OOP 
 - Inheritance  

 - Encapsulation 
 - Abstraction 
 - Polymorphism  


1. Inheritance : ref: parent class /child/sub class 

- allows a class to inherit attributes and methods from another class. This promotes code reuse : establishes a natural hierachy between classes 
 #### Key point 
 1. To access attributes use the super().__init__ to get value initialization 
 2. To acess methods , simply call the method '
 3. We can override the methods - 1. Create a method in the derived class with the same name as in the base class , 2. Give you different logic implementation.



