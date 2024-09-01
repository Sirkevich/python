class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name, surname, number_phone):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone

    def __str__(self):
        return f"{self.name} {self.surname} "


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_str = ""
        for item, count in self.products.items():
            items_str += f"{item.name}: {count} psc.\n"

        return (f"User: {self.user}\n"
                f"Items:\n"
                f"{items_str}")

    def get_total(self):
        self.total = 0
        for item, cnt in self.products.items():
            self.total += item.price * cnt

        return f"Total: {self.total}"


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5
print('-' * 100)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov
print('-' * 100)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print('-' * 100)

print(cart.get_total())
print(cart.get_total())
print('-' * 100)


cart.add_item(apple, 10)
print(cart)
print('-' * 100)

print(cart.get_total())
