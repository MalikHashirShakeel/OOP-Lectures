#-------------------------------------PARENT CLASS-----------------------------------------------------------

class Methods:

    class_var = "Class Inside."

    def __init__(self):
        self.instance = "Instance Variable."

    def instance_method(self):
        # Accessing class and instance varibles from inside the class.
        print(self.class_var) #Using instance
        print(self.instance)
        print(Methods.class_var) #Using class name

    @classmethod
    def class_method(cls):
        print(cls.class_var) #Using class address
        print(Methods.class_var) #Using class name
        # print(cls.instance) #This statement will raise error

    @staticmethod
    def static_method(class_variable,instance_variable):
        print(class_variable) #Printing class variable.
        print(instance_variable) #printing instance variable.

    def static_method_without_decorator(class_var,instance_var):
        print(class_var) #Printing class variable
        print(instance_var) #Printing instance variable

    def call_methods(self):
        self.instance_method()
        self.class_method()
        self.static_method(Methods.class_var,self.instance)
        # self.static_method_without_decorator(Methods.class_var,self.instance) #This statement will raise error because of self.

#-----------------------------------CHILD CLASS-------------------------------------------------------------

class Child(Methods):
    def __init__(self):
        super().__init__()
        self.instance_method()
        self.class_method()
        self.static_method(Methods.class_var,self.instance)
        # self.static_method_without_decorator(Methods.class_var,self.instance) #This statement will raise error because of self.

#-------------------------------------CLIENT CODE-----------------------------------------------------------

obj1 = Methods()
obj1.call_methods() #Accessing instance method from inside the class.
obj2 = Child() #Accessing instance method from child class.
obj1.static_method(Methods.class_var,obj1.instance)
obj2.static_method(Methods.class_var,obj1.instance)
Methods.static_method_without_decorator(Methods.class_var,obj1.instance)
# obj1.static_method_without_decorator(Methods.class_var,obj1.instance) #This will also raise error because obj1 will be passed in place of self and it does not take self as aegument.If you want to do it define @staticmethod decorator before the method. 
