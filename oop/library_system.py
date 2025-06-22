class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def str(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def init(self, title, author, file_size):
        super().init(title, author)
        self.file_size = file_size  # in KB

    def str(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def init(self, title, author, page_count):
        super().init(title, author)
        self.page_count = page_count

    def str(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def init(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book) 