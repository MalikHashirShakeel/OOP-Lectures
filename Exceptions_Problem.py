# def input_in_range(min,max):
#     while True:
#         number = int(input(f"Enter the number within the range({min} to {max}): "))
#         if min <= number <= max :
#             return number
#         print("Please enter the number within the given range.")

# def create_list(no_of_inputs,min,max):
#     l = []
#     for _ in range(no_of_inputs):
#         number = input_in_range(min,max)
#         l.append(number)
#     return l

# try:
#     f = open("MyFile.txt","w")
#     print("Opening file...")
#     list_of_inputs = create_list(5,1,100)
#     f.write(str(list_of_inputs))
#     print("List saved!")
#     print("Closing file...")
#     f.close()
# except Exception as e:
#     print(type(e),":",e)

#--------------------------------------------------VERSION 2------------------------------------------------------

# def input_in_range(min,max):
#     while True:
#         number = int(input(f"Enter the number within the range({min} to {max}): "))
#         if min <= number <= max :
#             return number
#         print("Please enter the number within the given range.")

# def create_list(no_of_inputs,min,max):
#     try:
#         l = []
#         for _ in range(no_of_inputs):
#             number = input_in_range(min,max)
#             l.append(number)
#     except Exception as e:
#         print(type(e),":",e)
#     return l

# try:
#     f = open("MyFile.txt","w")
#     print("Opening file...")
#     list_of_inputs = create_list(5,1,100)
#     f.write(str(list_of_inputs))
#     print("List saved!")
#     print("Closing file...")
#     f.close()
# except Exception as e:
#     print(type(e),":",e)

#---------------------------------------------------VERSION 3------------------------------------------------------

# def input_in_range(min,max):
#     while True:
#         number = int(input(f"Enter the number within the range({min} to {max}): "))
#         if min <= number <= max :
#             return number
#         print("Please enter the number within the given range.")

# def create_list(no_of_inputs,min,max):
#     l = []
#     for _ in range(no_of_inputs):
#         try:
#             number = input_in_range(min,max)
#             l.append(number)
#         except Exception as e:
#             print(type(e),":",e)
#     return l

# try:
#     f = open("MyFile.txt","w")
#     print("Opening file...")
#     list_of_inputs = create_list(5,1,100)
#     f.write(str(list_of_inputs))
#     print("List saved!")
#     print("Closing file...")
#     f.close()
# except Exception as e:
#     print(type(e),":",e)

#---------------------------------------VERSION 4-----------------------------------------------------------------

# def input_in_range(min,max):
#     try:
#         while True:
#             number = int(input(f"Enter the number within the range({min} to {max}): "))
#             if min <= number <= max :
#                 return number
#             print("Please enter the number within the given range.")
#     except Exception as e:
#         print(type(e),":",e)

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
#     f.write(str(list_of_inputs))
#     print("List saved!")
#     print("Closing file...")
#     f.close()
# except Exception as e:
#     print(type(e),":",e)

#-----------------------------------------------VERSION 5-----------------------------------------------------------

# def input_in_range(min,max):
#     while True:
#         try:
#             number = int(input(f"Enter the number within the range({min} to {max}): "))
#             if min <= number <= max :
#                 return number
#             print("Please enter the number within the given range.")
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
#     f.write(str(list_of_inputs))
#     print("List saved!")
#     print("Closing file...")
#     f.close()
# except Exception as e:
#     print(type(e),":",e)

#-------------------------------------------------VERSION 6--------------------------------------------------------

def input_in_range(min,max):
    while True:
        try:
            number = int(input(f"Enter the number within the range({min} to {max}): "))
            if min <= number <= max :
                return number
            print("Please enter the number within the given range.")
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
    f.write(str(list_of_inputs))
    print("List saved!")
except Exception as e:
    print(type(e),":",e)
finally:
    print("Closing file...")
    f.close()






