'''
ASSOCIATION
An obj of 1 class usses an obj of another class in it's method
'''


class Pen():
    def __init__(self, brand, color):
        self.color = color
        self.brand = brand

class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Student():
    def __init__(self, name, age, pen):
        self.name = name
        self.age = age
        self.pen = pen  #aggregation

    def read_book(self, book):  #association
        print(f"{self.name} is reading a {book.title} book by {book.author}")

    def write(self):
        print(f"{self.name} is writing using a {self.pen.brand} pen of {self.pen.color} ")


b1 = Book("half gf","chetan bagath")
b2 = Book("1947","fjsda hfui")
p1 = Pen("cello","Blue")
s1 = Student("fffggggg",14,p1)

s1.read_book(b1)
s1.read_book(b2)
s1.write()