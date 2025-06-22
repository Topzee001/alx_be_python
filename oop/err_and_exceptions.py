
    # # mastering exception handling
    # try:
    # # Code that might raise an exception
    # except ExceptionType:
    # # Code to handle the exception
    # else:
    # # Code that executes if no exception occurs
    # finally:
    # # Code that always executes, regardless of exceptions

# #   using raise statement to raise an exception
# def divide(x, y):
#   if y == 0:
#     raise ZeroDivisionError("Division by zero is not allowed")
#   return x / y

# # custom exceptions

# class OutOfStockError(Exception):
#     """Custom exception for handling out-of-stock items."""
#     def __init__(self, item_name):
#         self.item_name = item_name

#     def __str__(self):
#         return f"Sorry, the item '{self.item_name}' is out of stock."
    
#     # Sample Product Inventory
# Product_inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 0, # out of stock
#     "grapes": 3
# }

# def purchase_item(item, quantity):
#     try:
#         if Product_inventory[item] == 0:
#             raise OutOfStockError(item)
#         else:
#             print(f"Purchase successful: {quantity} {item}(s)")
#             Product_inventory[item] -= quantity
#     except KeyError:
#         print(f"Sorry, '{item}' is not available in our inventory.")

# # Testing the custom Exception
# try:
#     purchase_item('apple', 3) # sucessful purchase
#     purchase_item('orange', 1) # raises , so the try block end here.
#     purchase_item('beet', 4) # item not available, and the keyError except is skipped bcus 
#                              # the try block already successfully executed. except if the first 2 were removed
# except OutOfStockError as e:
#     print("this is the error: ", e)

# # print the updated contents of the inventory
# print(Product_inventory)

# # Exercise 1: Handling ZeroDivisionError



# def divide(num1, num2):
#     if num2 == 0:
#         raise ZeroDivisionError("Division by error is not allowed")
#     return num1/num2
    
# """ If a function raises an exception, and you don't want your 
# program to crash, you should call that function inside a 
# try-except block to handle the error."""
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = divide(num1, num2)
#     print("Result", result)
# except ZeroDivisionError as e:
#     print("Error: ", e)

# # Exercise 2: File Handling with FileNotFoundError

# try:
#     # file = open("examples.txt", 'r') # no indentation needed
#     # content = file.read() # or use 
#     with open("examples.txt", "r") as file: # indentation needed
#         content = file.read()
# except FileNotFoundError:
#     print("Error: file does not exist")
# else:
#     print(content)
# finally:
#     print("Execution completed\n")

# # for a file existence
# # create the file
# print("this is an existig file\n")
# with open("example.txt", "w") as f:
#     f.write("Hello, this is a test file.")

# try:
#     file = open("example.txt", 'r')
#     content = file.read()
# except FileNotFoundError:
#     print("Error: file does not exist")
# else:
#     print(content)
# finally:
#     print("Execution completed")

# Exercise 3: Custom Exception
# custom exceptions

class ValueTooHighError(Exception):
    def __init__(self, number):
        self.number = number
    
    def __str__(self):
        return f"Sorry, {self.number} is too high, number should not be greater than 100"

def check_number(num):
    if num > 100:
        raise ValueTooHighError(num)
    else:
        print(f"{num} is within range")


try:
    number = int(input("enter a number: "))
    check_number(number)
except ValueTooHighError as e:
    print(e)
except ValueError: #bonus to handle non int inputs
    print("invalid input! please enter an integer.")
