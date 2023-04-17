class Item:
    all : list  = []
    _discount = 1.0

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.amount})"

    def calculate_total_price(self):
        """return total price for certain items"""
        return round(self.price * self.amount)

    def apply_discount(self):
        """apply the discount for certain item"""
        print("price", self.price)
        print("discount", self.__class__._discount)
        self.price = round(self.price * self.__class__._discount)

    def set_discount(self, new_discount):
        """set the discount for all items"""
        self.__class__._discount = new_discount

