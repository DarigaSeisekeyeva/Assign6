class Goods:
    def __init__(self, registration, name, description, price):
        self.registration = registration
        self.name = name
        self.description = description
        self.price = price

    def display(self):
        print(f"Name: {self.name}, Description: {self.description}, Price: {self.price}")