"""
Q11: Online Shopping System.

Classes: Product, Customer, Cart, Order.
Features: add products, add/remove from cart, checkout, generate invoice.

Run with: python main.py
"""


class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.stock} in stock)"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Cart:
    def __init__(self):
        self.items = {}  # product_id -> quantity

    def add_item(self, product, quantity=1):
        self.items[product.product_id] = self.items.get(product.product_id, 0) + quantity

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def is_empty(self):
        return len(self.items) == 0


class Order:
    _next_order_id = 1

    def __init__(self, customer, line_items, total_amount):
        self.order_id = Order._next_order_id
        Order._next_order_id += 1
        self.customer = customer
        self.line_items = line_items  # list of (product, quantity, subtotal)
        self.total_amount = total_amount

    def generate_invoice(self):
        lines = [f"Invoice for Order #{self.order_id} — {self.customer.name}"]
        lines.append("-" * 45)
        for product, quantity, subtotal in self.line_items:
            lines.append(f"{product.name:<20} x{quantity:<3} = ₹{subtotal}")
        lines.append("-" * 45)
        lines.append(f"Total: ₹{self.total_amount}")
        return "\n".join(lines)


class ShoppingSystem:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, stock):
        self.products[product_id] = Product(product_id, name, price, stock)
        return f"Product '{name}' added"

    def checkout(self, customer, cart):
        if cart.is_empty():
            return None, "Error: cart is empty"

        line_items = []
        total_amount = 0
        for product_id, quantity in cart.items.items():
            product = self.products.get(product_id)
            if not product:
                return None, f"Error: product {product_id} no longer exists"
            if quantity > product.stock:
                return None, f"Error: not enough stock for '{product.name}'"
            subtotal = product.price * quantity
            line_items.append((product, quantity, subtotal))
            total_amount += subtotal
            product.stock -= quantity

        order = Order(customer, line_items, total_amount)
        return order, "Checkout successful"


def main():
    print("Q11: Online Shopping System")
    shop = ShoppingSystem()

    print(shop.add_product("P1", "Wireless Mouse", 499, 20))
    print(shop.add_product("P2", "Mechanical Keyboard", 2999, 10))
    print(shop.add_product("P3", "USB-C Hub", 1299, 15))

    customer = Customer("C1", "Neha Kapoor")
    cart = Cart()
    cart.add_item(shop.products["P1"], 2)
    cart.add_item(shop.products["P2"], 1)
    cart.add_item(shop.products["P3"], 1)
    cart.remove_item("P3")  # customer changes their mind

    order, message = shop.checkout(customer, cart)
    print("\n" + message)
    if order:
        print()
        print(order.generate_invoice())
        print("\nRemaining stock of Wireless Mouse:", shop.products["P1"].stock)


if __name__ == "__main__":
    main()
