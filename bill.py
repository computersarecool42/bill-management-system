import datetime
from meal import Meal
from drink import Drink
from service import Service


class Bill:
    """
    The Bill class represents a bill for a restaurant or similar establishment.

    Attributes:
        __entries (list): A list of entries (meals, drinks, services) on the bill.
        __log (list): A list of log entries for the bill.

    Methods:
        check_discount(overall_sum, discount): Calculates the discounted amount based on the overall sum and discount percentage.
        calculate_with_discount(discount): Calculates the total bill amount with the given discount percentage applied.
        calculate(): Calculates the total bill amount without any discounts.
        print_to_file(filename): Prints the bill details, including the date and all entries, to a file.
        add_meal(name, price): Adds a meal entry to the bill.
        add_drink(name, price): Adds a drink entry to the bill.
        add_services(name, price, guest_number): Adds a service entry to the bill.
    """
    def __init__(self):
        self.__entries = []
        self.__log = []

    @staticmethod
    def check_discount(overall_sum, discount):
        return overall_sum - overall_sum * discount / 100

    def calculate_with_discount(self, discount):
        current_sum = self.calculate()
        return current_sum - current_sum * discount / 100

    def calculate(self):
        cost = 0.0
        for meal in self.__entries:
            cost += meal.price
        return cost

    def print_to_file(self, filename):
        date = datetime.date.today()
        with open(filename, "w+") as file:
            file.write(f"Date: {date}\n")
            for entry in self.__entries:
                file.write(entry.generate_description())

    def add_meal(self, name, price):
        meal = Meal(name, price)
        self.__entries.append(meal)

    def add_drink(self, name, price):
        drink = Drink(name, price)
        self.__entries.append(drink)

    def add_services(self, name, price, guest_number):
        service = Service(name, price, guest_number)
        self.__entries.append(service)

    # Read
    @property
    def entries(self):
        return self.__entries

    # Write
    @entries.setter
    def entries(self, entries):
        if not entries:
            print("Entries can't be empty")
        else:
            self.__entries = entries

    # Write
    @property
    def log(self):
        return self.__log

    # Read
    @log.setter
    def log(self, log_entry):
        if not isinstance(log_entry, str):
            print("Log entry must be a string")
        else:
            self.__log.append(log_entry)