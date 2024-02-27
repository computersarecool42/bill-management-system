from routes import logic, form
from flask import Flask

web = Flask(__name__)
web.register_blueprint(logic.logic_routes)
web.register_blueprint(form.form_routes)

# Bill can not be global, because it has to be global for all runs of the app
# but data about chosen product are stored only in sessions
bill = None
user = None

if __name__ == '__main__':

    # Set a unique secret key to generate cookies for each user
    web.secret_key = "secret value"
    web.run(debug=True)
