
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self._cart = []

    def add_to_cart(self, product):
        self._cart.append(product)

    def remove_from_cart(self, product):
        try:
            self._cart.remove(product)
        except ValueError:
            print(f"{product.name} not found in cart.")

    def view_cart(self):
        if not self._cart:
            print("Your cart is empty.")
            return
        print("--- Your Cart ---")
        for product in self._cart:
            print(f"{product.name}: ${product.price}")

    def checkout(self):
        if not self._cart:
            print("Your cart is empty.")
            return
        total = sum(product.price for product in self._cart)
        print(f"--- Checkout ---\nTotal: ${total}")
        self._cart = []

class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def add_product(self, product):
        Catalog.products.append(product)

    def remove_product(self, product):
        try:
            Catalog.products.remove(product)
        except ValueError:
            print(f"{product.name} not found in catalog.")

    def update_product_price(self, product, new_price):
        try:
            product.price = new_price
        except AttributeError:
            print(f"{product} is not a valid product.")

class Catalog:
    products = []

    @classmethod
    def show_all_products(cls):
        if not cls.products:
            print("Catalog is empty.")
            return
        print("--- Product Catalog ---")
        for product in cls.products:
            print(f"{product.name}: ${product.price}, Stock: {product.stock}")

    @classmethod
    def find_product_by_name(cls, name):
        for product in cls.products:
            if product.name.lower() == name.lower():
                return product
        return None

#exaple
product1 = Product("Laptop", 1200, 10)
product2 = Product("Mouse", 25, 20)

Catalog.show_all_products()

admin = Admin("admin", "admin@example.com")
user = User("user", "user@example.com")
admin.add_product(product1)
admin.add_product(product2)
Catalog.show_all_products()

user.add_to_cart(product1)
user.view_cart()
user.checkout()