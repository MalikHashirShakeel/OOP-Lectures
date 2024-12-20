class Person:
    pass

a = Person()
print(isinstance(a,Person))

#------------------------------------------------------------------------------------------------------------

class Employee:
    pass

class Person:
    pass

class Programmer(Person,Employee):
    pass

print(issubclass(Programmer,Employee))

#-------------------------------------------------------------------------------------------------------------

obj = Programmer()
print(Programmer.__bases__)

#-------------------------------------------------------------------------------------------------------------

print(Programmer.__mro__)

#-----------------------------------ABCs in Python------------------------------------------------------------

from collections.abc import Container

#------------------------------------------EXAMPLE 1----------------------------------------------------------

class Employee2(Container):

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def __contains__(self, x):
        if x in self.name:
            return True
        else:
            return False
        
obj2 = Employee2("Hashir the kaamchor employee","420")
print("Hashir" in obj2)
print(isinstance(obj2,Employee))
print(issubclass(Employee2,Container))

#XX
#We can also use this without inheriting from conainer because python supports '''DUCK TYPING'''
#XX

class Employee3:

    def __init__(self,name,id):
        self.name = name
        self.id = id

    def __contains__(self, x):
        if x in self.name:
            return True
        else:
            return False 
        
obj3 = Employee2("Hashir the mehanti employee","786")
print("Hashir" in obj3)
print(isinstance(obj3,Employee))
print(issubclass(Employee3,Container))

#------------------------------------------EXAMPLE 2----------------------------------------------------------

class JoBhi(Container):

    def __contains__(self, x):
        return isinstance(x,int) and x%2 != 0
    
obj1 = JoBhi()
print(3 in obj1)
print(3.5 in obj1)
print(4 in obj1)
    
#-------------------------------------------PENCIL CLASS EXAMPLE----------------------------------------------

class Pencil:

    def __init__(self,color = None):
        self.__color = color

    def get_color(self):
        if self.__color != None:
            return self.__color
        else:
            return "Colour not set."
        
    def set_color(self,color):
        colors = ["kaala","neela","peela","hara"]
        if color in colors:
            self.__color = color
        else:
            pass

obj4 = Pencil()
obj4.set_color("kaala")
print(obj4.get_color())