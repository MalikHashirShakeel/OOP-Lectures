#----------------------------------------------VERSION 1-----------------------------------------------------------------
# try:
#     money = int(input("Enter the money: "))
#     shares = int(input("Enter the number of shares: "))
#     if shares == 1:
#         raise ValueError("Shares can't be equal to one.")
#     print(f"{money/shares}")
# except ValueError as ve:
#     print(f"{type(ve)}:{ve}")
# except ZeroDivisionError as zde:
#     print(f"{type(zde)}:{zde}")
# except Exception as e:
#     print(f"{type(e)}:{e}")
# except:
#     print("Something unusual happened.")
# print("GOODBYE!!!")


#---------------------------------------------VERSION 2------------------------------------------------------------------

# try:
#     money = int(input("Enter the money: "))
#     shares = int(input("Enter the number of shares: "))
#     if shares == 1:
#         raise ValueError("Shares can't be equal to one.")
#     print(f"{money/shares}")
# except Exception as e:
#     print(f"{type(e)}:{e}")
# print("GOODBYE!!!")

#--------------------------------------------VERSION 3-------------------------------------------------------------------

# while True:
#     try:
#         money = int(input("Enter the money: "))
#         shares = int(input("Enter the number of shares: "))
#         if shares == 1:
#             raise ValueError("Shares can't be equal to one.")
#         print(f"{money/shares}")
#         break
#     except Exception as e:
#         print(f"{type(e)}:{e}")
# print("GOODBYE!!!")

#----------------------------------------------VERSION 4------------------------------------------------------------------

while True:
    try:
        money = int(input("Enter the money: "))
        shares = int(input("Enter the number of shares: "))
        if shares == 1:
            raise ValueError("Shares can't be equal to one.")
        print(f"{money/shares}")
    except Exception as e:
        print(f"{type(e)}:{e}")
    else:
        break
    finally:
        print("GOODBYE!!!")
        