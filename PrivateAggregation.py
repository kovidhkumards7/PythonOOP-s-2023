'''
PRIVATE AGGREGATION
An object of 1 class been sent as a arguement to another class is called as ---------
'''

class Student():
    def __init__(self, name, age, pen):
        self.name = name
        self.age = age
        self.pen = pen

    def write(self):
        print(f"{self.name} is writing using {self.pen.brand} pen of {self.pen.color} color")

    def set_pen(self,pen):
        self.pen = pen

    def get_pen(self):
        return self.pen

class Pen():
    def __init__(self, brand, color):
        self.color = color
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_brand(self,brand):
        self.__brand = brand

p1 = Pen("Reynolds","green")
s1 = Student("sam",52,p1)
# s1.write()
# p1.color = "Blue"
# s1.write()
# s1.pen.color = "Black"
# s1.write()
p2 = Pen("Faber","Red")
# s1.pen = p2
# s1.write()
print("-----------------------------")
print(s1.pen.get_brand())
p1.set_brand("Indian")
print(s1.pen.get_brand())
print("-----------------------------")
s1.get_pen().color = "Red"
print(p1.color)
print("---------------------")
s1.set_pen(p2)
print(s1.pen.get_brand())