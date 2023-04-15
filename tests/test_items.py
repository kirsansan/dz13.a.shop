

def test_init_item(get_test_item, get_test_all):
    assert get_test_item.price == 5
    assert get_test_item.amount == 8
    assert get_test_all[1]._discount == 1.0

def test_print_all(get_test_all):
    assert str(get_test_all) == "[Item(NAME1,5,8), Item(NAME_not1,500,10)]"

def test_print(get_test_item):
    assert get_test_item.__repr__() == 'Item(NAME1,5,8)'

def test_set_discount(get_test_item):
    new_item = get_test_item
    assert new_item.price == 5
    new_item.discount == 0.1        # it's not Class discount, only local class instance
    assert new_item.discount == 0.1
    new_item.apply_discount()
    assert new_item.price == 5      # we don't have changes!!

    new_item.set_discount(0.3)      # now we have been changing
    new_item.apply_discount()
    assert new_item.price == 2


