from entry import Entry


class Meal(Entry):
    """
    The Meal class represents a meal item.

    :param str name: The name of the meal.
    :param float price: The price of the meal.
    """
    def __init__(self, name, price):
        super().__init__(name, price)

    # Converts a dictionary to a class instance, mapping keys to attributes and values accordingly.
    @classmethod
    def fromdict(self, dictionary):
        returnObject = Meal(None, None)
        for k, v in dictionary.items():
            setattr(returnObject, k, v)
        return returnObject
