# exercise 2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def product_attributes(self):
        product_details = f"{self.name} {self.price} {self.quantity}"
        return product_details

    def total_value(self):
        value = self.price * self.quantity
        return value

product1 = Product("book", 500, 2)
product2 = Product("pencil", 200, 9)

print(f"Total value of {product1.name}: ${product1.total_value()}")
print(f"Total value of {product2.name}: ${product2.total_value()}")

print(product1.product_attributes())
print(product1.name)