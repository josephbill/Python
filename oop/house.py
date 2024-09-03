# to create a class : CLASS 
# base class / parent class 
class House:
    # use the __init__ method to define the attributes that belong to the various instances created from this class.
    # the first param is always the self keyword : is a reference to the current instance of the class: used to access variables and methods that belong to the class. 
    '''
    1. First argument in instance methods , when defining the method its the first parameter 
    2. Accessing / Modification Instance variables / use access the class attributes 
    3. We can use to call other methods within the same class
    ''' 

    # class attributes
    name = "Joseph"

    def __init__(self,address,num_rooms,color,square_footage):
        # initialize our passed attributes 
        self.address = address
        self.num_rooms = num_rooms
        self.color = color
        # whenever an attribute is defined using the __ doubles underscores : private attribute 
        # it can only be modified from within the class 
        # provide a method to get the value attribute  
        self.__square_footage = square_footage #private attribute 
    

    # methods 
    def open_door(self):
        return f'The door of {self.address} is opened {self.name}'
    
    def turn_on_light(self):
        return f'The lights of {self.address.upper()} is turned on! {self.name}'
    
    # getter method 
    def get_square_footage(self): 
        return self.__square_footage
    
class SmartHouse:
    def __init__(self, has_security_system):
        self.has_security_system = has_security_system
        
    def activate_system(self):
        return "security system updated" if self.has_security_system else "no security system installed"
    
    def turn_on_light(self):
        return f'The lights of smart house'

# () derived class
class Mansion(House,SmartHouse):
    def __init__(self,address,num_rooms,color,square_footage,has_security_system,has_swimming_pool):
        # super is a keyword used to reference the base class in the derived class 
        House.__init__(self,address,num_rooms,color,square_footage)
        SmartHouse.__init__(self,has_security_system)
        self.has_swimming_pool = has_swimming_pool
        
    def turn_on_light(self,x):
        #  house,smarthouse
        # return my return by basing it off a conditional : if x == "house"  return elif x = "smarthouse"
        return House.turn_on_light(self) # or SmartHouse.turn_on_lights(self)
    
    # unique methods belonging to the derived class that are not in the parent class 
    def open_pool(self):
        return f"The swimming pool at {self.address} is now open!" if self.has_swimming_pool else 'No swimming pool available'
        
     

class Bungalow(House):
    pass

mansionA = Mansion("ABC Street",10,"blue","10sq",True,True)
mansionB = Mansion("ABC Street B",12,"Black","10sq",False,False)

# print(f"Mansion : {mansionA.address}")
# print(f"Mansion : {mansionB.address}")
print(mansionA.turn_on_light("house"))
# print(mansionB.open_pool())
# print(mansionB.has_security_system)
# print("before modification")
# print(mansionB.num_rooms)
# print("after modification")
# mansionB.num_rooms = 24
# print(mansionB.num_rooms)
# print("before modification")
# print(mansionB.__square_footage)
print(mansionB.get_square_footage())
print("sq modification")
mansionB.__square_footage = "70sq"
print(mansionB.__square_footage)

# print(mansionB.activate_system())

    
# ## CREATING THE OBJECT 
# mansion = House("ABC Street", 10, "white", "10sq")
# bungalow = House("CDE Street",3,"black","5sq")


# print(f'Mansion Address: {mansion.address} Room : {mansion.num_rooms}')
# print(f'Bungalow Address: {bungalow.address} Room : {bungalow.num_rooms}')
# print(mansion.turn_on_light())


