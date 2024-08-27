import ipdb

def add(a,b):
    return a + b

def divide(a,b):
    print(a,b)
    if b == 0:
        raise ValueError("cannot divide by 0")
    # # insertion of the ipdb breakpoint 
    ipdb.set_trace() # program stops here 
    return a/b 

print(divide(10,2))