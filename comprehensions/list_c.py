# input : [1,2,3,4,5,6,7,8,9,10]
# output : [1,4,9,16,25,36,49,64,81,100]
# return a new list where each element has been squared
# traditional loop 
def squarenumbers(x):
    end_output = []
    for a in x:
        square_result = a**2
        end_output.append(square_result)
        
    return end_output

print(squarenumbers([1,2,3,4,5,6,7,8,9,10]))

x = [a**2 for a in range(1,11)]
print(x)        


# make my output contain only even squares 
# [4,16,36,64,100]
# [expressions for item in iterable if condition]
even_x = [a**2 for a in range(1,11) if a % 2 == 0]
print(even_x)        

