class Cus():
    c = 0
    def __init__(self,name,loc):
        self.name = name
        self.__loc = loc
        self.reward = 600
        Cus.c += 1

    def pur(self,amt):
        print(f"pur done for {self.name} at the cost of {amt}")

    def get_loc(self):
        return self.__loc

    def set_loc(self,loc):
        self.__loc = loc

a = Cus("vdsgv fds","fbsa")
b = Cus("gfdfszdzssa fds","fs")

a.pur(524)
b.pur(5258)
print(a.name)
print(a.get_loc())
print(a.set_loc("fs"))
print(a.get_loc())
print(a.reward)
print(b.name)
print(b.get_loc())
print(b.set_loc("15315ds"))
print(b.get_loc())
print(b.reward)
print(Cus.c)
print("----------------------------------")
print(a._Cus__loc)
a._Cus__loc = "hdfsbaf sajf ns"
print(a._Cus__loc)