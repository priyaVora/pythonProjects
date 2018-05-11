from model.item import Item
class Store(object):
    """This Store Class represents each event taking place in a given time.
           Each event holds one nformation about itself. A Store holds list of items and shopping cart
           A Store provides functionality to add items to cart, to check if a given item is in a cart.
           Also it provides functionality to check how items in the cart, and check the total price of item(s)."""
    def __init__(self,items):
        """This Store Class represents each event taking place in a given time.
                   Each event holds one nformation about itself. A Store holds list of items and shopping cart
                   A Store provides functionality to add items to cart, to check if a given item is in a cart.
                   Also it provides functionality to check how items in the cart, and check the total price of item(s)."""
        self.items = items
        self.__shopping_cart = {}

    def add_cart(self, item, quantity):
        if self.is_in_cart(item) == False:
            self.__shopping_cart[item] = quantity

    def is_in_cart(self, item):
       if item in self.__shopping_cart:
           return True
       else:
           return False

    def get_cart_items(self):
        print("All items will be returned")
        list = []
        for each_item in self.__shopping_cart:
            list.append(each_item)
        return list

    def get_cart_item_quantity(self, item):
        if self.is_in_cart(item) == True:
            quantity = self.__shopping_cart[item]
            return quantity
        else:
            return 0
        print(l)

    def total_price(self, *option):

        if option:
            if self.is_in_cart(option[0]) == True:
                passed_item = option[0]
                quantity_of_item = self.get_cart_item_quantity(passed_item)
                total_price = quantity_of_item * passed_item.price
                return total_price
            else:
                price = option[0].price
                return price
        else:
            total_price = 0
            for each_item in self.__shopping_cart:
                quantity_of_item = self.get_cart_item_quantity(each_item)
                price_of_current_item = each_item.price * quantity_of_item
                total_price += price_of_current_item
            return total_price




