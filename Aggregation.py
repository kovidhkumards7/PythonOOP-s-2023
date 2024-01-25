'''
AGGREGATION
An object of 1 class been sent as a arguement to another class is called as ---------
'''

class Student():
    def __init__(self, name, age, pen):
        self.name = name
        self.age = age
        self.pen = pen

    def write(self):
        print(f"{self.name} is writing using {self.pen.brand} pen of {self.pen.color} color")

class Pen():
    def __init__(self, brand, color):
        self.color = color
        self.brand = brand

p1 = Pen("Reynolds","green")
s1 = Student("sam",52,p1)
s1.write()
p1.color = "Blue"
s1.write()
s1.pen.color = "Black"
s1.write()
p2 = Pen("Faber","Red")
s1.pen = p2
s1.write()