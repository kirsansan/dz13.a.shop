class Item:
    all = []
    discount = 0.85
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
