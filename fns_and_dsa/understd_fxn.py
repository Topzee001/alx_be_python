# name = 'topzee'
# - function definition
# Exercise 1: Write a function to greet the user by name.
# def greet(name):
# #   """Prints a greeting message."""
#   print(f"Hello, {name}!")

# greet(name)

#  - lambda function
# add = lambda x, y : x + y

# print(add(5,4))


# - parameters
# Exercise 2: Create a function to calculate the area of a rectangle.
# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))

# def calculate_area(length, width):
#     area = length * width
#     # print(f"the area of the rectangle is: {area}")
#     return area

# result = calculate_area(length, width)
# print(f"the area of the rectangle is: {result}")

# - Passing argument
# calculate_area(10, 5)  # rectangle_area will be 50

# # - Keyword Arguments
# def user_info(name, age=None):
#     print(f"Name: {name}")
#     if age:
#         print(f"Age: {age}")
#     return age

# result = user_info(name="Bob", age=20)

# print(f"this is the result {result}")

# # - Default values
# # Function definition with default value
# def greet(name="World"):
#      """Prints a greeting message."""
#      print(f"Hello, {name}!")
# greet()  # Output: Hello, World!
# greet("Alice")  # Output: Hello, Alice! 

# # Return values
# def square(number):
#      """Returns the square of a number."""
#      return number * number
# squared_value = square(4)
# print(squared_value)

# # # variable scope ad functions
# # - local and global scope

# count = 0 #global variable
# def increment():
#     count +=1 # local count within the function, didn't declare the count, so when the function is called, there will b error
#     print(count)

#     increment()

# print(f"global count: {count}")

# # - global and nonlocal keywords
# # modifying global variable from a fxn
# count = 0
# def incremen_global():
#     global count
#     count +=1
# incremen_global()
# print(f"modified global count: {count}")

# # using non local keyword to modify enclosing fxn
# def outer_fxn():
#     x = 10 #variable in an encloing function

#     def inner_fxn():
#         nonlocal x
#         x +=5
#     inner_fxn()
#     print("modified value of x from inner fxn:", x)
# outer_fxn()

# # Exercise3: Develop a function to check if a number is even or odd.

# def checkType(num):
#     if num % 2 == 0:
#         print(f"{num} is an even number")
#     else:
#         print(f"{num} is an odd number")

# print("check if a number is even or odd")
# num = int(input("enter a number: "))
# checkType(num)

# # alternate solution to exercise 3
# def checkType(num):
#     return "even" if num % 2 == 0 else "odd"

# print("check if a number is even or odd")
# num = int(input("enter a number: "))
# result = checkType(num)
# print(f"{num} is an {result} number")

