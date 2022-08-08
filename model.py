from unicodedata import name


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def validate_password(self, password):
        return self.password == password
    