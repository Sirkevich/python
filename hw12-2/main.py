from inspect import isgenerator


class Item:

    def __init__(self, name, price, description, dimensions, color, material, warranty):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.color = color
        self.material = material
        self.warranty = warranty

    def __str__(self):
        return f"{self.name}, price: {self.price}"
                # f"Description: {self.description}\n"
                # f"Dimensions: {self.dimensions}\n"
                # f"Color: {self.color}\n"
                # f"Material: {self.material}\n"
                # f"Warranty: {self.warranty}\n")


class User:

    def __init__(self, name, surname, number_phone, age, gender):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.name} {self.surname}"
                # f"Number_phone: {self.number_phone}\n"
                # f"Age: {self.age}\n"
                # f"Gender: {self.gender}\n")


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
        pass


lemon = Item("lemon", 5, "fruit", "small", "yellow", None, None)
apple = Item("apple", 10, "fruit", "medium", "red", None, None)
# box = Item("box", 10, "packing box", "large", "brown", "cardboard", 1)
# print(lemon)  # lemon, price: 5
# print(apple)
# print(box)
buyer = User("Ivan", "Ivanov", "02628162", 25, 'male')
# buyer_02 = User("Stepan", "Bandera", "02628321", 18, 'male')
# buyer_03 = User("Roman", "Shukhevych", "02645162", 20, 'male')
# print(buyer)  # Ivan Ivanov
# print(buyer_02)
# print(buyer_03)
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
#
# assert cart.get_total() == 40
