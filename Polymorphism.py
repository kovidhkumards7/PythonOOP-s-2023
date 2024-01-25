'''
Dynamic Polymorphism(Method Overriding), possible only with inheritence
'''

class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print(f"I am {self.name}, I can fly")



class Penguin(Bird):
    def fly(self):
        super().fly()
        print("Penguins don't fly")

peng1 = Penguin("Owl")
peng1.fly()

b1 = Bird("Parrot")