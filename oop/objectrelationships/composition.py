# is a stronger form of aggregation. 
# Implies ownership , meaning that the contained objects cannot exist 
# independently of the containing object 

# Car and Engine 
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        

class Car:
    def __init__(self, model, engine_horsepower):
        
        self.model = model 
        # composition : Car owns Engine 
        self.engine = Engine(engine_horsepower)
        
    def display(self):
        print(f"{self.model} car has an engine with {self.engine.horsepower}")
        

# car has a strong ownership over the Engine 
my_car = Car("Tesla", 670)
my_car.display()