class Invoice():
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __gt__(self, other):
        if self.amt > other.amt:
            return True
        return False

    def __ge__(self, other):
        if self.amt > other.amt:
            return True
        return False

    def __str__(self):
        return (f"{self.amt} , {self.name}")

b1 = Invoice("fsd",4165)
b2 = Invoice("sfsdxgvdf",12)

print(b1>b2) # > operator from class
print(b1>=b2) # > = operator from class

print(b1) # __str__ operator from class

print(help(list))
print(dir(list))
