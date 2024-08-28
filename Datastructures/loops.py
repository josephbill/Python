fruits = ["apple","banana","orange"]
def functioncall(fruit):
    print(f"{fruit} is nice")
    
for fruit in fruits:
    functioncall(fruit)
    print(fruit)
    
## range , output the current index in iteration 
fruitrange = len(fruits)

for i in range(fruitrange):
    print(fruits[i])

## while 
count = 0
while count < 6 :
    print(count)
    count += 1
    
### break : exits a loop prematurely 
### continue : skips the rests of the current iterations and moves on to the next iterations (based on a condition)
## nested loops 
### For each outer iteration nested loop complete the full cycle of the inner iterations
for i in range(3):
    for j in range(2):
        print(f'i={i}, j={j}')
        