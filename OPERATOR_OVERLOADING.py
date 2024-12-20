#----------------------------------------IN CLASS PROB1------------------------------------------------------------

# class Concatination:

#     def __init__(self,var1 = ""):
#         self.var1 = var1

#     def __add__(self,var2):
#         return self.var1 + str(var2)
    
# obj = Concatination("Computer")
# print(obj + [1,2,3])

#----------------------------------------IN CLASS PROB2(c)-----------------------------------------------------

# class Point:

#     def __init__(self ,xcoord = 0, ycoord = 0):
#         self.xcoord = xcoord
#         self.ycoord = ycoord

#     def __str__(self):
#         return f"<{self.xcoord} , {self.ycoord}>"
    
#     def __add__(self,p):
#         return f"<{self.xcoord + p.xcoord} , {self.ycoord + p.ycoord}>"
    
# p1 = Point(1,1)
# p2 = Point(2,2)
# print(p1 + p2)

#-------------------------------------IN CLASS PROB2(d)------------------------------------------------------------

# class Point:

#     def __init__(self ,xcoord = 0, ycoord = 0):
#         self.xcoord = xcoord
#         self.ycoord = ycoord

#     def __str__(self):
#         return f"<{self.xcoord} , {self.ycoord}>"
    
#     def __add__(self,p):
#         self.xcoord += p.xcoord
#         self.ycoord += p.ycoord
#         return self
    
# p1 = Point(1,1)
# p2 = Point(2,2)
# print(p1 + p2)

#-------------------------------------IN CLASS PROB2(e)-------------------------------------------------------

# class Point:

#     def __init__(self ,xcoord = 0, ycoord = 0):
#         self.xcoord = xcoord
#         self.ycoord = ycoord

#     def __str__(self):
#         return f"<{self.xcoord} , {self.ycoord}>"
    
#     def __neg__(self):
#         self.xcoord = -self.xcoord
#         self.ycoord = -self.ycoord
#         return self

# p1 = Point(2,2)
# print(-p1)

#----------------------------------------IN CLASS PROB3---------------------------------------------------------------

from math import sqrt

class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.xcoord = xcoord
        self.ycoord = ycoord

    def __str__(self):
        return f"<{self.xcoord}, {self.ycoord}>"
    
    def __neg__(self):
        self.xcoord = -self.xcoord
        self.ycoord = -self.ycoord
        return self

class Line:
    def __init__(self, point1, point2):
        if isinstance(point1, Point):
            self.point1 = point1
        else:
            self.point1 = Point(0, 0)

        if isinstance(point2, Point):
            self.point2 = point2
        else:
            self.point2 = Point(0, 0)

    def __invert__(self):
        return sqrt((self.point2.xcoord - self.point1.xcoord)**2 + (self.point2.ycoord - self.point1.ycoord)**2)

p1 = Point(1, 1)
p2 = Point(2, 2)
l1 = Line(p1, p2)
print(~l1)


        


