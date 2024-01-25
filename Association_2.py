class Payment:
    counter = 0
    def __init__(self, payment_mode):
        self.payment_mode = payment_mode
        self.transaction_id = 0
    def validate_payment_mode(self):
        if self.payment_mode in ('Cash', 'Card', 'Net Banking', 'UPI'):
            return True
        return False
    def generate_transaction_id(self):
        if (self.validate_payment_mode()):
            Payment.counter += 1
            self.transaction_id = 1000 + Payment.counter
        else:
            self.transaction_id = -1


class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = []
    def add_to_cart(self, product):
        self.shopping_cart.append(product)
        print(f'Product {product.prod_name} of price {product.price} is added to the cart')
    def display_cart(self):
        if len(self.shopping_cart) == 0:
            print(f'Cart is empty')
            return
        print(f'Displaying cart of {self.name}')
        for index in range(len(self.shopping_cart)):
            prod = self.shopping_cart[index]
            print(f'{index+1}. {prod.prod_name} {prod.manufacturer} {prod.price}')
    def make_payment(self, payment_mode, amount):
        payment = Payment(payment_mode) # Association
        payment.generate_transaction_id()
        if (payment.transaction_id==-1):
            print(f'Invalid payment mode selected')
        else:
            print(f'Payment of amount {amount} by {payment_mode} is successful')


class Product:
    def __init__(self, prod_name, manufacturer, price):
        self.prod_name = prod_name
        self.manufacturer = manufacturer
        self.price = price

p1 = Product('Bluetooth speaker', 'JBL', 8999)
p2 = Product('Chips', 'Lays', 30)
p3 = Product('Maggi', 'Nestle', 85)
c1 = Customer('Pragya')
# c1.display_cart()
# c1.add_to_cart(p1)
# c1.add_to_cart(p2)
# c1.add_to_cart(p3)
# c1.display_cart()
c1.make_payment('Cash', 7899.78)
c1.make_payment('cash', 7899.78)