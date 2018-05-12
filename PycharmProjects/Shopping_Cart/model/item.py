

class Item(object):
    """This Item Class represents each item being sold im a specific store.
    Each item holds three different information about itself. An item has a name, description
    and price allocated to itself."""
    def __init__(self, name, description, price):
        """This Item Class represents each item being sold im a specific store.
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
        item_representation = "$%.2f :: %s :: %s" % (self.price, self.name, self.description)
        return str(item_representation)


    __repr__ = __str__


