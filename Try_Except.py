#-------------------------------------------Version 1----------------------------------------------------------------------

# divident = int(input("Enter the divident here: "))
# divisor = int(input("Enter the divisor here: "))
# print(f"{divident}/{divisor} = {divident/divisor}")
# print("Have a good day.")

#-------------------------------------------Version 2-----------------------------------------------------------------------

# try:
#     divident = int(input("Enter the divident here: "))
#     divisor = int(input("Enter the divisor here: ")) 
#     print(f"{divident}/{divisor} = {divident/divisor}")
# except:
#     print("Wrong input!!!")
# print("Have a good day.")

#-------------------------------------------Version 3----------------------------------------------------------------------

# try:
#     divident = int(input("Enter the divident here: "))
#     divisor = int(input("Enter the divisor here: ")) 
#     print(f"{divident}/{divisor} = {divident/divisor}")
# except ValueError:
#     print("Please enter valid input.")
# except ZeroDivisionError:
#     print("The divisor must not be zero.")
# except:
#     print("Something unusual happened.")
# print("Have a good day.")

#--------------------------------------------Version 4---------------------------------------------------------------------

# try:
#     divident = int(input("Enter the divident here: "))
#     divisor = int(input("Enter the divisor here: ")) 
#     print(f"{divident}/{divisor} = {divident/divisor}")
# except ValueError as ve:
#     print(f"Value Error : {ve}")
# except ZeroDivisionError as zde:
#     print(f"Zero division error : {zde}")
# except:
#     print("Something unusual happened.")
# print("Have a good day.")

#----------------------------------------------Version 5--------------------------------------------------------------------

try:
    divident = int(input("Enter the divident here: "))
    divisor = int(input("Enter the divisor here: ")) 
    print(f"{divident}/{divisor} = {divident/divisor}")
except ValueError as ve:
    print(f"Value Error : {ve}")
except ZeroDivisionError as zde:
    print(f"Zero division error : {zde}")
except KeyboardInterrupt as ke:
    print(f"Keyboard interrupt : {ke}")
except Exception as e:
    print(f"Exception : {e}")
except:
    print("Something unusual happened.")
print("Have a good day.")

#---------------------------------------------------------------------------------------------------------------------------