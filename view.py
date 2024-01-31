"""
This module provides functions to interactively ask the user for inputs related to meals, drinks, services, discounts, and filenames.
Each function prompts the user and returns the entered values, with proper validation and error handling.

Functions:
    ask_for_meal(): Asks the user for a meal's name and price. Returns a tuple (name, price) if valid inputs are provided, otherwise (None, None).
    ask_for_drink(): Asks the user for a drink's name and price. Returns a tuple (name, price) if valid inputs are provided, otherwise (None, None).
    ask_for_service(): Asks the user for a service's name, price, and the number of guests. Returns a tuple (name, price, guest_number) if valid inputs are provided, otherwise (None, None, None).
    ask_for_check_discount(): Asks the user for the total sum and discount percentage. Returns a tuple (overall_sum, discount) if valid inputs are provided, otherwise (None, None).
    ask_for_discount(): Asks the user for a discount percentage. Returns the discount as an integer if a valid input is provided, otherwise None.
    ask_for_filename(): Asks the user for a filename. Returns the filename as a string.
"""


def ask_for_meal():
    name = input("Provide meal name: ")
    price = input("Provide meal price: ")
    try:
        return name, float(price)
    except ValueError:
        print("Unable to add a meal, you need to provide a valid price")
        return None, None


def ask_for_drink():
    name = input("Provide drink name: ")
    price = input("Provide drink price: ")
    try:
        return name, float(price)
    except ValueError:
        print("Unable to add a drink, you need to provide a valid price")
        return None, None


def ask_for_service():
        name = input("Provide meal name: ")
        price = input("Provide meal price: ")
        guest_number = input("Provide guest number: ")
        try:
            return name, float(price), int(guest_number)
        except ValueError:
            print("Unable to proceed, you need to provide valid inputs (price and guest number should be numerical)")
            return None, None, None


def ask_for_check_discount():
    overall_sum = input("Provide total sum: ")
    discount = input("Provide discount percentage: (%): ")
    try:
        return float(overall_sum), int(discount)
    except ValueError:
        print("Unable to proceed, you need to provide valid inputs (overall sum and discount should be numerical)")
        return None, None


def ask_for_discount():
    discount = input("Provide discount percentage: (%): ")
    try:
        return int(discount)
    except ValueError:
        print("Unable to proceed, you need to provide valid input (discount should be numerical)")
        return None


def ask_for_filename():
    filename = input("Provide filename: ")
    return filename




