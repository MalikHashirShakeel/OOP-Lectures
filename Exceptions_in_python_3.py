# class OutOfRangeError(Exception):
#     pass

# def input_in_range(min,max):
#     while True:
#         try:
#             number = int(input(f"Enter the number within the range({min} to {max}): "))
#             if min <= number <= max :
#                 return number
#             raise OutOfRangeError("Please Enter the value wothin the given range.")
#         except Exception as e:
#             print(type(e),":",e)

# def create_list(no_of_inputs,min,max):
#     l = []
#     for _ in range(no_of_inputs):
#             number = input_in_range(min,max)
#             l.append(number)
#     return l

# try:
#     f = open("MyFile.txt","w")
#     print("Opening file...")
#     list_of_inputs = create_list(5,1,100)
#     print("List saved!")
# except BaseException as be:
#     print(type(be),":",be)
# else:
#     f.write(str(list_of_inputs))
# finally:
#     print("Closing file...")
#     f.close()

#---------------------------------VERSION 2-----------------------------------------------------------------------

class OutOfRangeError(Exception):
    def __init__(self,message = "Pleaase enter the value within the given range."):
        self.message = message
        super().__init__(message)

def input_in_range(min,max):
    while True:
        try:
            number = int(input(f"Enter the number within the range({min} to {max}): "))
            if min <= number <= max :
                return number
            raise OutOfRangeError
        except Exception as e:
            print(type(e),":",e)

def create_list(no_of_inputs,min,max):
    l = []
    for _ in range(no_of_inputs):
            number = input_in_range(min,max)
            l.append(number)
    return l

try:
    f = open("MyFile.txt","w")
    print("Opening file...")
    list_of_inputs = create_list(5,1,100)
    print("List saved!")
except BaseException as be:
    print(type(be),":",be)
else:
    f.write(str(list_of_inputs))
finally:
    print("Closing file...")
    f.close()