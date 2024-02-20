class User:
    def __init__(self):
        self.__auth = {
            "username": "bruno",
            "password": "cycki123"
        }

        self.__preferences = {
            "theme": "light"
        }

    def login(self, username, password):
        if username == self.__auth["username"] and password == self.__auth["password"]:
            return True
        else:
            return False

    @property
    def auth(self):
        return self.__auth

    @auth.setter
    def auth(self, value):
        self.__auth = value

    @property
    def preferences(self):
        return self.__preferences

    @preferences.setter
    def preferences(self, value):
        self.__preferences = value
