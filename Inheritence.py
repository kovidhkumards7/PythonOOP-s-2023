class Bird():
    def __init__(self,name):
        self.name = name

    def fly(self):
        print(f"I am {self.name}, I can fly")


class Swarrow(Bird):
    def __init__(self,loc,name):
        super().__init__(name)
        self.loc = loc
        print("swarrow constructor")

    def fly(self):
        print(f"Sparrow is flying in {self.loc}")

    def display(self):
        print(f"I am {self.name} bird from {self.loc}")

# b1 = Bird("vndj")
# b1.fly()
sp1 = Swarrow(name = "spa1",loc = "Africa")
sp1.fly()
sp1.display()