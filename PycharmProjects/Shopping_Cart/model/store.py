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

       # print("Does item contain in the cart already?-" + str(self.is_in_cart(item)))
        if self.is_in_cart(item) == False:
            value = None
        else:
            value = self.__shopping_cart.get(item)
        if self.is_in_cart(item) == False:
            value = self.__shopping_cart.get(item)
            #print("Value Before " + str(value))
            self.__shopping_cart[item] = quantity
        elif self.is_in_cart(item) == True:
            self.__shopping_cart[item] = quantity + value
            #print("Quantity of item now: " + str(self.get_cart_item_quantity(item)))

    def is_in_cart(self, item):
       if item in self.__shopping_cart:
           return True
       else:
           return False

    def get_cart_items(self):
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

    def remove_from_cart(self, item, *quantity):
        print(quantity)
        if quantity:
            quantity_to_remove = quantity[0]
            if quantity_to_remove == 0:
                del self.__shopping_cart[item]
            elif quantity_to_remove <= self.get_cart_item_quantity(item):

                value = self.get_cart_item_quantity(item) - quantity_to_remove
                print("removed : " + str(quantity_to_remove))
                self.__shopping_cart[item] = value
            elif quantity_to_remove > self.get_cart_item_quantity(item):
                self.__shopping_cart[item] = 0

            if self.get_cart_item_quantity(item) == 0:
                self.__shopping_cart.pop(item, None)
                #del self.__shopping_cart[item]
            #print("Quantity of item: " + str(item.name) + ": " + str(self.get_cart_item_quantity(item)))
            #print("Quantity to remove: " + str(quantity_to_remove))
        else:
            del self.__shopping_cart[item]
            #print("Quantity of item: " + str(item.name) + ": " + str(self.get_cart_item_quantity(item)))


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

