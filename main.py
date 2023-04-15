from items.items import Item

if __name__ == '__main__':
    item1 = Item("car", 10_000, 2)
    item2 = Item("phone", 1_000, 60)
    # print(item1)
    print(item1.calculate_total_price())
    print(item2.calculate_total_price())

    #Item.discount = 0.8
    item1.set_discount(0.9)
    item1.apply_discount()
    print(item1.price)
    print(item2.price)

    print(Item.all)