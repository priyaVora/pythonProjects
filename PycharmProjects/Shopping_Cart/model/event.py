from model.item import Item

class Event(Item):
    """This Event Class represents each event taking place in a given time.
        Each event holds four different information about itself. An item has a name, description
        price, date allocated to itself."""
    def __init__(self, name, description, price, date):
        """This Event Class represents each event taking place in a given time.
                Each event holds four different information about itself. An item has a name, description
                price, date allocated to itself."""
        self.date = date
        super(Event, self).__init__(name, description,price)
    def __str__(self):
        item_representation = "%s :: %s :: $%.2f :: %s" % (self.name, self.date,self.price, self.description)
        return item_representation

Event("Cup", "You use to drink in", 0.345, "5/4/3").__str__()
