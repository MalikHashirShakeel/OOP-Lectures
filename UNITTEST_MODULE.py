from unittest import TestCase,main

def average(lst):
    try:
        assert isinstance(lst,list),"The input must be a list type object"
        assert len(lst) != 0 ,"The list must have atleast one element in it." 
        return round(sum(lst) / len(lst),2)
    except AssertionError as e:
        print(e)
    
class AverageTset(TestCase):

    def testcase_1(self):
        self.assertEqual(average([40,40,40]),40.0)

    def testcase_2(self):
        self.assertEqual(average([3,4,5]),4.0)

    def testcase_3(self):
        self.assertEqual(average([]),None)

main()

#--------------------------------------------VERSION 2----------------------------------------------------------------

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
    
# class AreaCheck(TestCase):

#     def testcase_1(self):
#         obj = Circle(2)
#         self.assertEqual(obj.find_area(),12.57)

#     def testcase_2(self):
#         obj = Circle(-2)
#         self.assertEqual(obj.find_area(),3.14)

# main()
