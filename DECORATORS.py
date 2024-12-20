#----------------------------------------PRACTICE------------------------------------------------------------------

# def decorator(func):
#     def wrapper():
#         print("Good Morning.")
#         func()
#         print("Good Night.")
#     return wrapper

# @decorator
# def func():
#     print("My name is Hashir.")

# func()

#-----------------------------------------PRACTICE------------------------------------------------------------------

def decorator(func):
    def wrapper(*args,**kwargs): #args kwargs are optional
        print("Good Morning.")
        func(*args,**kwargs)  #args kwargs are optional
        print("Good Night.")
    return wrapper

def func(a,b):
    print(a + b)

func(2,3)

#-------------------------------------------------------------------------------------------------------------

