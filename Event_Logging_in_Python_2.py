# import logging

# logging.basicConfig(filename = "test.log",format= "%(asctime)s : %(levelname)s : %(name)s : %(message)s",level = logging.DEBUG)

# def take_input():
#     value = input("Enter a number here: ")
#     if value.isalpha():
#         logging.warning("This input may cause error.")
#         return value
#     else:
#         logging.info("True value entered!")
#         return float(value)
    
# value = take_input()
# try:
#     division = 1 / value
# except ValueError:
#     logging.error("invalid value entered.",exc_info = True)
# except ZeroDivisionError:
#     logging.error("Division by zero.",exc_info = True)
# except:
#     logging.error("Something went wrong.",exc_info = True)

#-------------------------------------------VERSION 2-----------------------------------------------------------------------

import logging

l = logging.getLogger("Logger By Hashir.")
l.setLevel(logging.DEBUG)
handler = logging.FileHandler("myLog.log","a")
formatter = logging.Formatter("%(asctime)s : %(funcName)s : %(levelname)s : %(message)s")
handler.setFormatter(formatter)
l.addHandler(handler)

def take_input():
    value = input("Enter a number here: ")
    if value.isalpha():
        l.warning("This input may cause error.")
        return value
    else:
        l.info("True value entered!")
        return float(value)
    
value = take_input()
try:
    division = 1 / value
except ValueError:
    l.error("invalid value entered.",exc_info = True)
except ZeroDivisionError:
    l.error("Division by zero.",exc_info = True)
except:
    l.error("Something went wrong.",exc_info = True)
