import random

# Exercise 1: List of Fruits
# Task: Create a list of favorite fruits, print the second element.
fruits = ["Mango", "Apple", "Banana", "Pineapple"]

# Access the second element (index 1 because Python lists are zero-indexed)
print("Second fruit in the list is:", fruits[1])

# Exercise 2: Dictionary of Book Info
# Task: Define a dictionary with book details and retrieve the genre.
book = {
    "title": "Atomic habits",
    "author": "James Clear",
    "genre": "Self-help"
}

# retrieving the genre using the get() method
print("The genre of the book is: ", book.get("genre"))

# Exercise 3: Random Set of Unique Numbers
# Task: Generate random numbers between 1 and 10, remove duplicates using set, and display them.
numbers = [random.randint(1, 10) for _ in range(15)] #generate 15 random numbers between 1 to 10

# remove dublicates using set
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)