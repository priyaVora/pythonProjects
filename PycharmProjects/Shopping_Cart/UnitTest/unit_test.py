import unittest
from faker import Faker
fake = Faker('en_US')


from model.store import Store
from model.store import Item
from model.event import Event
from assignment1.__main__ import print_items_in_cart
from assignment1.__main__ import print_items_in_store
from assignment1.__main__ import add_item_to_cart
from assignment1.__main__ import remove_item_from_cart
from assignment1.__main__ import checkout

class ShoppingCartTest(unittest.TestCase):
#
    def generate_data(self):
        list = []
        input_file = open("input.txt", 'w')
        for each_item in range(0, 20):
            item = Item(fake.name(), fake.address(), fake.random_int(min=0, max=999))
            list.append(item)
            print(item)

            input_file.write(str(item).replace("\n", ""))
            input_file.write("\n")
            print("---")
        for each_event in range(0,5):
            event = Event(fake.name(), fake.address(),fake.random_int(min=0, max=999),fake.date_time_between_dates(datetime_start=None, datetime_end=None, tzinfo=None))
            print(event)
            input_file.write(str(event).replace("\n", ""))
            input_file.write("\n")
            list.append(event)
        input_file.close()
        return list

    # @unittest.skip("Test Later")
    def test_print_items_in_store(self):
        list = self.generate_data()
        store = Store(list)
        print_items_in_store(store)
        store_list = store.items
        self.assertEqual(list,store_list)

    def test_print_items_in_cart(self):
        list = self.generate_data()
        store = Store(list)

        for each_item in list:
            store.add_cart(each_item, 1)
        print_items_in_cart(store)
        self.assertEqual(list,store.get_cart_items())

    # @unittest.skip("Test Later")
    def test_add_items_to_cart(self):
        list = self.generate_data()
        store = Store(list)
        for each_item in list:
            store.add_cart(each_item, 1)
        add_item_to_cart(store)
        self.assertEqual(list,store.get_cart_items())


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