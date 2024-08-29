# creates a new set by applying an expression to each item in an iterable 
# similar to lists only that it removes duplicates 
# {expression for item in iterable if condition}

unique_set = set()
for x in [1,2,2,2,3,33,3,4,5,6,7]:
    unique_set.add(x**2)
  
print(unique_set)  

unique_set_c = {x**2 for x in [1,2,2,2,3,33,3,4,5,6,7] }
print(unique_set_c)

# suppose you have a list of words and you want to find the unique lengths of those words 
# use a set comprehension to achieve the same 
# input : ["apple", "banana","Cherry", "grape", "apple", "apple", "orange"]
# output : {5,6}