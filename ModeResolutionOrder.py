class A():
    def sample(self):
        print("Sample of class A")

class B():
    def sample(self):
        print("Sample of class B")

class C(A,B):
    pass
    # def sample(self):
    #     print("Sample C")

c = C()
c.sample()
print(C.mro())