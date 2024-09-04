# 1,1,2
fibonnacci_solutions = {}
def fibonnacci(n):
    #isInstance of : n: integer : -negative integer
    if n in fibonnacci_solutions:
        return fibonnacci_solutions[n]
    
    if n == 1:
      return 1 
    elif n == 2: 
      return 1
    else:
        #recursion f(n : 1) = F(n-1) + F(n-2) for n > 2 
        value = fibonnacci(n - 1) + fibonnacci(n-2)
        # dynamic key creation
    fibonnacci_solutions[n] = value
    return value
  
  

for n in range(1,500):
    print(n , ":" , fibonnacci(n))
    
    
# above is not optimized due to redudant calculations