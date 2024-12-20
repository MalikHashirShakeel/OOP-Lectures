# from time import time

# def decorator(func):
#     def modified_func():
#         time_1 = time()
#         func()
#         time_2 = time()
#         print(f"Time taken : {round(time_2 - time_1,2)} sec")
#     return modified_func

# @decorator
# def calc_time():
#     input("Press any key to calculate the time: ")

# calc_time()

#------------------------------------------EXAMPLE2(PARAMETERIZED FUNCTION)----------------------------------

def decorator(function):
    def modified_function(*args,**kwargs):
        avg = function(*args,**kwargs)
        if avg >= 6:
            print("Congratulations Beta hua h.XD")
        else:
            print("I am sorry :(")
    return modified_function

@decorator
def average(quiz1,quiz2):
    return (quiz1 + quiz2) / 2

average(8,8.5)
