# from class_static_methods_demo import Calculator

# def main():
#     # Using the static method
#     sum_result = Calculator.add(10, 5)
#     print(f"The sum is: {sum_result}")

#     # Using the class method
#     product_result = Calculator.multiply(10, 5)
#     print(f"The product is: {product_result}")

# if __name__ == "__main__":
#     main()

# # for book_class.py project

# from book_class import Book

# def main():
#     # Creating an instance of Book
#     my_book = Book("1984", "George Orwell", 1949)

#     # Demonstrating the __str__ method
#     print(my_book)  # Expected to use __str__

#     # Demonstrating the __repr__ method
#     print(repr(my_book))  # Expected to use __repr__

#     # Deleting a book instance to trigger __del__
#     del my_book

# if __name__ == "__main__":
#     main()

# for library_system.py project
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()