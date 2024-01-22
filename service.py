from entry import Entry


class Service(Entry):
    """
    The Service class represents a service item.

    :param name: The name of the service.
    :param price: The price of the service.
    :param guest_number: The number of guests for the service.
    """
    def __init__(self, name, price, guest_number):
        super().__init__(name, price)
        self.guest_number = guest_number

    def generate_description(self):
        return f"Product: {self.name}, Price: {self.price}, Guests: {self.guest_number}\n"

