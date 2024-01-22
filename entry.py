class Entry:
    """
    The Entry class represents an entry in a product list.

    It encapsulates information about a product, including its name
    and price. It provides a method to generate a description of the product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.

    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def generate_description(self):
        return f"Product: {self.name}, Price: {self.price}\n"