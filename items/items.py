class Item:
    all = []
    discount = 1.0

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.amount})"

    def calculate_total_price(self):
        return round(self.price * self.amount)

    def apply_discount(self):
        self.price = round(self.price * self.__class__.discount)

if __name__ == '__main__':
    item1 = Item("car", 10_000, 2)
    item2 = Item("phone", 1_000, 60)
    # print(item1)
    print(item1.calculate_total_price())
    print(item2.calculate_total_price())

    Item.discount = 0.8
    item1.apply_discount()
    print(item1.price)
    print(item2.price)

    print(Item.all)

