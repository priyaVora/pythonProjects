from model.item import Item

class Event(Item):
    """This Event Class represents each event taking place in a given time.
        Each event holds four different information about itself. An event has a name, description
        price, date allocated to itself."""
    def __init__(self, name, description, price, date):
        """This Event Class represents each event taking place in a given time.
                Each event holds four different information about itself. An event has a name, description
                price, date allocated to itself."""
        self.date = date
        super(Event, self).__init__(name, description,price)
    def __str__(self):
        item_representation = "$%.2f :: %s :: %s :: %s" % (self.price, self.date,self.name, self.description)
        return str(item_representation)

    __repr__ = __str__


