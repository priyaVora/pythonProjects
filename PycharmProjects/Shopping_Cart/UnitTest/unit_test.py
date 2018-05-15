import unittest

from model.store import Store
from model.store import Item
from assignment1.__main__ import print_items_in_cart
from assignment1.__main__ import print_items_in_store
from assignment1.__main__ import add_item_to_cart
from assignment1.__main__ import remove_item_from_cart
from assignment1.__main__ import checkout

class ShoppingCartTest(unittest.TestCase):

    def generate_data(self):
        priya = Item("Priya", "Friend", 0.345)
        priyanki = Item("Priyanki", "Friend", 0.745)
        ankita = Item("Ankita", "Friend", 0.95)
        nainesh = Item("Nainesh", "Friend", 10.2)
        list = [priya, priyanki, ankita, nainesh]
        return list


    def test_print_items_in_store(self):
        list = self.generate_data()
        store = Store(list)
        print_items_in_store(store)

    @unittest.skip("Test Later")
    def test_print_items_in_cart(self):
        list = self.generate_data()
        store = Store(list)
        print_items_in_cart(store)

    @unittest.skip("Test Later")
    def test_add_items_to_cart(self):
        list = self.generate_data()
        store = Store(list)
        add_item_to_cart(store)

    @unittest.skip("Test Later")
    def test_remove_item_from_cart(self):
        list = self.generate_data()
        store = Store(list)
        remove_item_from_cart(store)

    @unittest.skip("Test Later")
    def test_checkout(self):
        list = self.generate_data()
        store = Store(list)
        checkout(store)