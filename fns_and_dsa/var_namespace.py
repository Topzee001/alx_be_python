# # Exercise 1: Local vs Global Scope Instruction:

# count = 10  # Global variable

# def outer_function():
#   count = 5  # Local variable within outer_function

#   def inner_function():
#     count = 2  # Local variable within inner_function
#     print(f"Inner function: {count}")  # Accesses local count (2)

#   inner_function()
#   print(f"Outer function: {count}")  # Accesses local count (5)

# print(f"Global scope: {count}")  # Accesses global count (10)

# outer_function()

# # Exercise 2: Namespace Exploration Instruction:
# count = 5

# def counting_function():
#     count = 5
#     print("Counting function - count ", count)

# def logging_function():
#     count = "Number of logs: 3" #count used as log description
#     print("Logging Function - count:", count)

# counting_function()
# logging_function()

# Exercise 3: Scope Hierarchy Instructions solution

x = 5 #this 'x' is in the global namespace

def first_function():
    #Enclosing/local scope
    x = 7 # this 'x' is in the local namespace of first_function

    print("first function local scope:", x) # python checks here first, because of the LEGB rule

       # To access the global 'x', we use 'global' keyword or 'globals()'
    print("global scope variable:", globals()['x']) # prints global x variable

first_function()

print("outside function, global x:", x)