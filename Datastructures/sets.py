my_set = {1,2,3,4,5,5,6,7}
print(my_set)
## adding .push 
my_set.add(8)
print(my_set)
# remove elements in the set 
# .remove() : reaises a KeyError if the element is not found 
my_set.remove(7)
print(my_set)
# .discard() : will not raise any error if the element is not found 
my_set.discard(10)
# pop()
print(my_set.pop())
## access of elements is via loops or the concept of list comprehensions.

[my_set,1,"Joseph"]

for x in my_set:
    print(x)






