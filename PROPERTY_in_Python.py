#-------------------------------------By Using Property Class------------------------------------------------

#COLOUR PENCIL EXAMPLE

class Pencil:

    def __init__(self,color = None):
        self.set_color(color)
        
    def set_color(self,color):
        color_list = ["red","blue","green","black"]
        if color in color_list:
            self.__color = color
        else:
            print("Invalid color!")
            self.__color = None

    def get_color(self):
        if self.__color != None:
            return self.__color
        else:
            return "Color not set."
        
    def deleter(self):
        del self.__color
        print("Color successfully deleted!")

    color = property(get_color,set_color,deleter,"You can get color, set color and also delete color.")

obj = Pencil("green")
print(obj.color)
print(type(Pencil.color))
obj.color = "red"
print(obj.color)
del(obj.color)
# print(obj.color) #ERROR!!!
obj.color = "blue"
print(obj.__dir__())
print(obj.__dict__)

#--------------------------------------USING PROPERTY DECORATOR-------------------------------------------------

# class Pencil:

#     def __init__(self,color = None):
#         self.color = color
        
#     @property
#     def color(self):
#         '''You can get color, set color and also delete color.'''
#         if self.__color != None:
#             return self.__color
#         return "Color not set!!!"

#     @color.setter
#     def color(self,color):
#         color_list = ["red","blue","green","black"]
#         if color in color_list:
#             self.__color = color
#         else:
#             print("Invalid color!")
#             self.__color = None
        
#     @color.deleter
#     def color(self):
#         del self.__color
#         print("Color successfully deleted!")

# obj2 = Pencil("orange")
# obj2.color = "green"
# print(obj2.color)
# del(obj2.color)
# # print(obj2.color) #This statement will give error
# obj2.color = "red"
# print(obj2.color)
# print(obj2.__dict__)
# print(obj2.__dir__)
# print(help(obj2))
        