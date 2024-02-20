# In this file are all the routes related to logic form
from routes.logic import get_bill, login_required
from user import User
from flask import Blueprint, session, render_template


form_routes = Blueprint('form_routes', __name__)


@login_required
@form_routes.route("/add_meal_form")
def add_meal_form():
    return render_template('add_meal_form.html')


@login_required
@form_routes.route("/add_services_form")
def add_services_form():
    return render_template('add_services_form.html')


@login_required
@form_routes.route("/check_discount_form")
def check_discount_form():
    bill = get_bill()
    return render_template('check_discount_form.html', calculation_result=bill.calculate())


@login_required
@form_routes.route("/apply_discount_form")
def apply_discount_form():
    bill = get_bill()
    return render_template('apply_discount_form.html', calculation_result=bill.calculate())


@form_routes.route("/login_form")
def login_form():
    user = User()
    # Clear all cookies when reaching the login form
    # session.clear()
    if 'auth' in session:
        print("Cookies are here!")
        auth = session['auth']
        user.auth = auth
        return render_template('dashboard_form.html')
    else:
        return render_template('login_form.html')


@login_required
@form_routes.route('/preferences_form')
def preferences_form():
    return render_template('preferences_form.html')


@form_routes.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')


@login_required
@form_routes.route("/dashboard_form")
def dashboard_form():
    return render_template('dashboard_form.html')
