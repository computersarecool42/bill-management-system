# In this file are all the routes related to logic processing
from datetime import datetime
from functools import wraps
from bill import Bill
from user import User
from flask import Blueprint, request, session, redirect, render_template, url_for, flash, abort

logic_routes = Blueprint('logic_routes', __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'auth' not in session:
            return redirect(url_for('form_routes.login_form'))
        return f(*args, **kwargs)

    return decorated_function


@logic_routes.route("/")
def index():
    if 'auth':
        return render_template('layout.html')
    else:
        return redirect(url_for('form_routes.login_form'))


@logic_routes.route("/login_check", methods=['POST'])
def login_check():
    user = User()

    username = request.form['username']
    password = request.form['password']

    if user.login(username, password):
        print("Correct Password!")
        session['auth'] = user.auth
        print(session['auth'])
        return redirect(url_for('form_routes.dashboard_form'))
    else:
        print("Incorrect Password!")
        flash("Incorrect credentials!", 'error')  # pass the error message through Flask's flash message system
        return redirect(url_for('form_routes.login_form'))


@logic_routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('form_routes.login_form'))


@logic_routes.route("/add_meal", methods=['POST'])
def add_meal():
    bill = get_bill()

    meal_name = request.form['meal_name']
    try:
        meal_price = float(request.form['meal_price'])
    except ValueError:
        return redirect(url_for('form_routes.add_meal_form', message="Unable to convert price"))

    bill.add_meal(meal_name, meal_price)
    # Update session with new products
    session['entries'] = bill.entries

    # Redirect to the add_meal_form after adding a meal
    return redirect(url_for('form_routes.add_meal_form'))


@logic_routes.route("/add_services", methods=['POST'])
def add_services():
    bill = get_bill()

    meal_name = request.form['meal_name']
    guest_number = request.form['guest_number']
    meal_price = float(request.form['meal_price'])

    bill.add_services(meal_name, meal_price, guest_number)
    # Update session with new products
    session['entries'] = bill.entries

    # Redirect to the add_meal_form after adding a meal
    return redirect(url_for('form_routes.add_services_form'))


@logic_routes.route("/check", methods=['POST'])
def check():
    discount_percentage = float(request.form['discount'])
    bill = get_bill()  # Retrieve or recalculate the bill amount.
    amount = bill.calculate()
    discounted_amount = bill.check_discount(amount, discount_percentage)

    # You can then pass the discounted_amount back to a template, redirect, or handle as needed.
    return render_template('default_template.html',
                           message=f"The overall sum with discount would be: {discounted_amount}")


@logic_routes.route("/apply_discount", methods=['POST'])
def apply_discount():
    discount_percentage = float(request.form['discount'])
    bill = get_bill()  # Retrieve or recalculate the bill amount.
    discounted_amount = bill.calculate_with_discount(discount_percentage)

    # You can then pass the discounted_amount back to a template, redirect, or handle as needed.
    return render_template('default_template.html',
                           message=f"The overall sum with applied discount: {discounted_amount}")


@logic_routes.route('/theme', methods=['POST'])
def theme():
    user = User()
    session['theme'] = request.form.get('theme')
    print(session['theme'])
    return redirect(request.referrer)


@login_required
@logic_routes.route("/sum_order")
def sum_order():
    # return render_template("404.html", message="Page not found!"), 404
    bill = get_bill()
    return render_template('default_template.html', message=f"The overall sum is: {bill.calculate()}")


@logic_routes.route("/save/<filename>")
def save(filename):
    bill = get_bill()
    try:
        bill.print_to_file(filename)
        return render_template("default_template.html", message="Success!")
    except:
        return render_template("default_template.html", message="Unable to save to file!")


@logic_routes.route("/contact", methods=['POST'])
def send_message():
    user_name = request.form['user_name']
    user_text = request.form['user_text']
    filename = f"Contact{datetime.now}.txt"
    with open(filename, "w") as file:
        file.writelines(f"Name: {user_name}, Message: {user_text}")
    return render_template("default_template.html", message="Your message was saved!")


def get_bill():
    bill = Bill()
    # Check if there are already any products in session
    # If yes, assign those products to object bill
    if 'entries' in session:
        entries = session['entries']
        bill.entries = entries
    return bill
