'''
this function prints a message before and after execution of a function
'''
# decorator 
def myDecorator(func):
    def anotherfunction():
        print('b4 fucntion runs')
        func()
        print('after function runs')
    
    return anotherfunction

@myDecorator
def simpleExecution():
    print('this is a simple print')
   
@myDecorator 
def another_function():
    print('this is a simple print from another function')

simpleExecution()

'''
decorators with arguments 
'''
def repeat(num_times):
    def decorator_repeat(func):
        # args . kwargs :: allows our decorator logic to accept any number of positional and keyword arguments 
        def decorator_arg(*args, **kwargs):
            for _ in range(num_times):
                # print(x)
                func(*args, **kwargs)
        return decorator_arg
    return decorator_repeat
        
@repeat(num_times=3)
def greetsUser(name):
    print(f'Hello, {name}')
    
greetsUser("Joseph")

'''
1. two functions : one divides , two : takes in a list of numbers , index position , 
log out element in that index position
Possible exceptions
1. Division by 0
2. Not a number 
3. empty list / index error // index is out of range 

'''
def decorator_exception(default_return_value=None):
    # this handles the exception in the specified function 
    def decorator(func):
        def decorator_args(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'Exception occurred in {func.__name__}: {e}')
                return default_return_value
        return decorator_args
    return decorator
            
            

@decorator_exception(default_return_value="Error: Division by 0")
def divide(a,b):
    return a/b 

@decorator_exception(default_return_value=None)
def get_item(data,index):
    return data[index]

print(
divide(10,0))

print(get_item([1,2,3],5))

