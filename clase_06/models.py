from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username, name, password):
        self.id = username
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<User {self.id}>'

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


users = {
    "ramses": User("ramses", "Ramsés", "ramses123"),
    "susana": User("susana", "Susana", "susana123"),
    "john": User("john", "John", "password")
}
