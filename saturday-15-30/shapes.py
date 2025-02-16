import math


class Shape:
    def area(self):
        pass

    def length(self):
        pass

    def __str__(self):
        return (
            "Shape has a length of "
            + str(self.length())
            + " and an area of "
            + str(self.area())
        )


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def length(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def length(self):
        return 2 * (2 * math.pi * self.radius)


circle = Circle(2)


class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return self.name + ", " + self.author + ", " + str(self.year)


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("List of books:")
        for book in self.books:
            print(book)


library = Library()
book = Book("War and Peace", "Lev Tolstoi", 1867)
library.add_book(book)
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
library.list_books()


def mult(a, b):
    return a * b


# print(mult(1,2))
