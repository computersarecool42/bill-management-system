from entry import Entry


class Drink(Entry):
    """
    The Drink class represents a drink item.

    :param name: The name of the drink.
    :param price: The price of the drink.
    """
    def __init__(self, name, price):
        super().__init__(name, price)
