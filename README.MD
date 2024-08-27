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