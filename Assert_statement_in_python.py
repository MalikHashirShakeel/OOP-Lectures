#------------------------------------------PROBLEM 1-----------------------------------------------------------------

# def average(lst):
#     try:
#         assert isinstance(lst,list),"The input must be a list type object"
#         assert len(lst) != 0 ,"The list must have atleast one element in it." 
#         return sum(lst) / len(lst)
#     except AssertionError as e:
#         return e

# print(average([1,2,3]))
# print(average([]))
# print(average(""))

#-----------------------------------------PROBLEM 2------------------------------------------------------------------

# from math import pi

# class Circle:

#     def __init__(self,radius = 1):
#         try:
#             assert isinstance(radius,int) ,"Radius must be int type object."
#             assert radius > 0,"Radius must be a positive integer."
#             self.radius = radius
#         except AssertionError as e:
#             self.radius = 1

#     def find_area(self):
#         return round(pi * self.radius ** 2,2)
    
# obj1 = Circle(2)
# print(obj1.find_area())
# obj2 = Circle(-1)
# print(obj2.find_area())

#----------------------------------------PROBLEM 3-----------------------------------------------------------
try:
    f = open("Myfile.txt")
    data = f.read()
    assert data != "","There is no data in the file."
    content = eval(data)
    assert isinstance(content,list),"The file content must be of list type"
    print(content)
    print(len(content))
    f.close()
except AssertionError as ae:
    print(f"{type(ae)} = {ae}")
    f.close()
except NameError:
    try:
        content = data
        assert isinstance(content,list),"The file content must be of list type"
        print(content)
        print(len(content))
        f.close()
    except Exception as e:
        print(f"{type(e)} = {e}")
except Exception as e:
    print(f"{type(e)} = {e}")

