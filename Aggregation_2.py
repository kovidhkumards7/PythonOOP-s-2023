class Product():
    def __init__(self,pname,pmanufacturer,pprice):
        self.pname = pname
        self.pmanufacturer = pmanufacturer
        self.pprice = pprice

class Customer():
    def __init__(self,name):
        self.name = name
        self.shoppingCart = []

    def addToCart(self,product):
        self.shoppingCart.append(product)
        print(f"{product.pname} of price {product.pprice} is added to cart")

    def displayCart(self):
        print(f"displaying cart of {self.name}")
        if (len(self.shoppingCart) == 0):
            print("u r cart is empty")
        for i in range(len(self.shoppingCart)):
            prod = self.shoppingCart[i]
            print(f"{i+1}-{prod.pname}-{prod.pmanufacturer}-{prod.pprice}")

p1 = Product("fs","dfsuyha",468)
p2 = Product("gd","bgfvhd",6345)
p3 = Product("asdf","sghdjhjykyukm",254)

c1 = Customer("fsbn dhsabd sdb")
c1.displayCart()
c1.addToCart(p1)
c1.addToCart(p2)
c1.addToCart(p3)
c1.displayCart()