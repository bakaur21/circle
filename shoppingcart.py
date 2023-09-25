#Write a Python program to create a class representing a shopping cart. 
#Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}  # A dictionary to store items and their quantities

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total = 0
        for item_name, item_info in self.items.items():
            total += item_info['price'] * item_info['quantity']
        return total

    def view_cart(self):
        for item_name, item_info in self.items.items():
            print(f"{item_name}: {item_info['quantity']} x ${item_info['price']} each")

# Example usage:
cart = ShoppingCart()

cart.add_item("Item 1", 10.99)
cart.add_item("Item 2", 5.99, 3)
cart.add_item("Item 3", 2.99)

cart.view_cart()

print("Total Price:", cart.calculate_total())

cart.remove_item("Item 2")
cart.view_cart()
