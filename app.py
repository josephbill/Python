# global scope : a variable created at the top level of a script or outside any function 
# Local scope : a variable created inside a function , and it can only accessed withing that function
# Enclosing scope : This scope exists in a nested function, the enclosing scope is the scope of the outer function
# that encloses the nested function
# Built in scope : This scope is reserved for python's built in functions (len, print)
global_Var = "I am Global"

def functionname():
    local_var = "I am local"
    print(global_Var)
    print(local_var)
    

functionname()
print(global_Var)
# print(local_Var)

def outer_function():
    
    enclosing_var = "I am enclosing"
    def inner_function():
        inner_var = "inner value function variable"
        print(enclosing_var)
    # print(inner_var)
    inner_function()
    
outer_function()

# using inbuilt 

print(len(global_Var))
    

#  to loop a string 
message = "hello"
list_e = []
for char in message:
    list_e.append(char)
    print(char)
    
print(list_e)
    
## zip :; allows us to loop two or more lists(or other iterables/sequences) in parallel
names = ["joseph","alice"] 
scores = ["30", "40"]
for name,score in zip(names,scores):
    print(f'{name} : scored {score}')

