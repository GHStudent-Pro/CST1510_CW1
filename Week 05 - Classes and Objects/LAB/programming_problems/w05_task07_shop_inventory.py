# Task 7: Shop Inventory


class Product:
    """A product with a name, price and quantity in stock."""

    def __init__(self, name, price, quantity):
        """Store the product details on the object."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Return price x quantity."""
        return self.price * self.quantity

    def apply_discount(self, percent):
        """Reduce this product's price by the given percentage."""
        self.price = self.price * (1 - percent / 100)


inventory = [
    Product("Laptop", 799.99, 5),
    Product("Mouse", 19.99, 40),
    Product("Keyboard", 49.50, 20),
    Product("Monitor", 159.00, 8),
    Product("USB Cable", 4.99, 100),
]

total = sum(product.total_value() for product in inventory)
print(f"Total inventory value: £{total:.2f}")

print("\nAfter a 10% discount:")
for product in inventory:
    product.apply_discount(10)
    print(f"  {product.name:<10} £{product.price:.2f}")
