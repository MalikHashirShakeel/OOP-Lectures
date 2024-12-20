#--------------------------------Defining Circle as a ReadWrite Property--------------------------------------------

# class Circle:

#     def __init__(self,radius = 1):
#         self.radius = radius

#     @property
#     def radius(self):
#         "Docstring will come here."
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r > 0:
#             self.__radius = int(r)
#         else:
#             self.__radius = 1

# #CLIENT CODE:
# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7.5
# print(obj.radius)
# print(type(obj.radius))
# print(type(Circle.radius))


#---------------------------------------------READ ONLY PROPERTY----------------------------------------------

# class Circle:
    
#     def __init__(self,radius):
#         if radius > 0:
#             self.__radius = int(radius)
#         else:
#             self.__radius = 1

#     @property
#     def radius(self):
#         "Docstring will come here."
#         return self.__radius
    
#     @radius.setter
#     def radius(self,_):
#         print("You cannot set the radius after setting it once.")

# # #CLIENT CODE:
# obj = Circle(6.5)
# print(obj.radius)
# obj.radius = 5

# #--------------------------------------------WRITE ONLY PROPERTY------------------------------------------------ 

# class Circle:

#     def __init__(self,radius):
#         self.radius =  radius

#     @property
#     def radius(self):
#         "Docstring will come here."
#         return "You cannot read the write only property."

#     @radius.setter
#     def radius(self,r):
#         if r > 0:
#             self.__radius = int(r)
#         else:
#             self.__radius = 1

# # #CLIENT CODE:
# obj = Circle(5)
# print(obj.radius)
# obj.radius = 6.5


# #-------------------------------------------Adding another property (diagonal)-----------------------------------

# class Circle:

#     def __init__(self,radius = 1,diagonal = 2):
#         self.radius = radius
#         self.diameter = diagonal

#     @property
#     def radius(self):
#         "Docstring will come here."
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r > 0:
#             self.__radius = int(r)
#         else:
#             self.__radius = 1

#     @property
#     def diameter(self):
#         "Docstring will come here."
#         return self.__diagonal
    
#     @diameter.setter
#     def diameter(self,d):
#         if d == self.radius * 2:
#             self.__diagonal = d
#         else:
#             self.radius = int(d / 2)
#             self.__diagonal = d

# # #CLIENT CODE:
# obj = Circle(5,6)
# print(obj.radius)
# print(obj.diameter)
# obj.diameter = 10
# print(obj.diameter)
# print(obj.radius)



# #----------------------------------------OVERRIDING THE PROPERTY IN CHILD CLASS(using abstract class)-----------

from abc import ABC,abstractproperty

class Circle(ABC):

    def __init__(self,radius):
        self.radius = radius

    @abstractproperty
    def radius(self):
        "Docstring will come here."
        return self.__radius
    
    @radius.setter
    def radius(self,r):
        if r > 0:
            self.__radius = int(r)
        else:
            self.__radius = 1

# #Version 1
# class PrecisedCircle(Circle):

#     @property
#     def radius(self):
#         "Docstring will come here."
#         return self.__radius
    
#     @radius.setter
#     def radius(self,r):
#         if r > 0:
#             self.__radius = r
#         else:
#             self.__radius = 1

# #Version 2
class PrecisedCircle(Circle):
    radius = 1


#CLIENT CODE
obj = PrecisedCircle(3)
print(obj.radius)
obj.radius = 5.4
print(obj.radius)
print(type(Circle.radius))

#--------------------------------------------------------------------------------------------------------------

    
