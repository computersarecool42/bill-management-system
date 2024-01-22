import datetime
from view import ask_for_meal, ask_for_discount, ask_for_filename, ask_for_service, ask_for_check_discount, \
    ask_for_drink
from bill import Bill


def main():
    """
    Main function for the Bill Management System.

    It interacts with the user by presenting them with a menu of options for managing their bill.
    The user can add meals, drinks, services, calculate the total bill amount, check available discounts,
    apply discounts, save the bill to a file, and view the log.

    :return: None
    """
    bill = Bill()
    action = "Start"

    while action != "9":
        action = input(
            "\n--- Bill Management System ---\n"
            "1. Add Meal\n"
            "2. Add Drink\n"
            "3. Add Service\n"
            "4. Sum\n"
            "5. Check Available Discount\n"
            "6. Apply Discount\n"
            "7. Save Bill\n"
            "8. View Log\n"
            "9. End\n"
            "-----------------------------\n"
            "Your choice (number): "
        )

        if action == "1":
            name, price = ask_for_meal()
            if name is None or price is None:
                continue
            bill.add_meal(name, price)
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "2":
            name, price = ask_for_drink()
            if name is None or price is None:
                continue
            bill.add_drink(name, price)
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "3":
            name, price, guest_number = ask_for_service()
            if name is None or price is None or guest_number is None:
                continue
            bill.add_services(name, price, guest_number)
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "4":
            total = bill.calculate()
            print("Total bill amount:", total)
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "5":
            overall_sum, discount = ask_for_check_discount()
            if overall_sum is None or discount is None:
                continue
            print(Bill.check_discount(overall_sum, discount))
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "6":
            discount = ask_for_discount()
            if discount is None:
                continue
            print("Total bill amount with discount:", bill.calculate_with_discount(discount))
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "7":
            filename = ask_for_filename()
            bill.print_to_file(filename)
            bill.log = action + f" - {datetime.datetime.now()}"
        elif action == "8":
            print(bill.log)


if __name__ == '__main__':
    main()
