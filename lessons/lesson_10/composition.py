class Author:
    
    def __init__(self, name:str, nationality:str):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name}"
        
class Book:
    
    def __init__(self, title:str, genre:str, author:Author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    
    def __init__(self, name:str):
        self.name = name
        self.books = []

    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        print(f"Available books:")
        for book in self.books:
            print(book)

    def remove_book(self, title:str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return 
        print(f"No book found with title {title}")
        

author_1 = Author("X", "hungarian")
author_2 = Author("Y", "russian")

book_1 = Book("Test book 1", "crime", author_1)
book_2 = Book("Test book 2", "crime", author_2)

print(book_1)
print(book_2)

lib_1 = Library("Szabó Ervin városi könyvtár")
lib_1.add_book(book_1)
lib_1.add_book(book_2)
print(lib_1.books)

lib_1.list_books()