print(sorted(("Rahul","Kovidh","Rishab","Aman"), key=len))
print("-------------------------")
def mul(fac):
    def mull(x):
        return x * fac
    return mull
a = mul(2)
print(a(7))
