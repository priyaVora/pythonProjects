

class Item(object):
    """This Item2 Class represents each item being sold im a specific store.
    Each item holds three different information about itself. An item has a name, description
    and price allocated to itself."""
    def __init__(self, name, description, price):
        """This Item1 Class represents each item being sold im a specific store.
        Each item holds three different information about itself. An item has a name, description
        and price allocated to itself."""

        self.name = name
        self.description = description


        try:
            self.price = float(price)
        except ValueError:
            self.price = self.price
        self.__str__()

    def __str__(self):
        item_representation = "%s :: $%.2f :: %s" % (self.name, self.price, self.description)
        return item_representation




