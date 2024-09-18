## Encapulsation : 
binding both data(attributes) and methods. 
combine data and subroutines to a class and restrict external access to the data.

### Designing classes and objects 
attributes and methods.

class Car:
     <!-- attributes :make. model. -->
     def __init__(self,make,model):
         <!-- defining the attributes as private members -->
         self.__make = make
         self.__model = model


    <!-- getter and setter methods -->
    <!-- use of the @property decorator :  -->
    @property
    def Model(self):
        return(self.__model)
    @Model.setter
    def Model(self,modelname):
        self.__model = modelname

<!-- creating the obj -->
obja = Car("x","y")
<!-- settings will allow changes -->
obja.Model("z")
<!-- getter -->
obja.Model()

methods :
1. what type of ACCESS / RESTRICTION TO ATTRIBUTES. 