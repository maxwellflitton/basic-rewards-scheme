from werkzeug.security import generate_password_hash

from run import app_instance


class User(app_instance.db.Model):
    """
    This is a class for managing the User model for the database.
    """

    __table_args__ = {'extend_existing': True}

    id = app_instance.db.Column(app_instance.db.Integer, primary_key=True)
    username = app_instance.db.Column(app_instance.db.String(80), unique=True, nullable=False)
    email = app_instance.db.Column(app_instance.db.String(120), unique=True, nullable=False)
    password = app_instance.db.Column(app_instance.db.String(128))

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes the password for checking and being saved.

        :param password: (str) password to be hashed
        :return: (str) hashed password
        """
        return generate_password_hash(password=password)

    def check_password(self, password: str) -> bool:
        """
        Checks the password to see if it matches the User's password.

        :param password: (str) password to be checked
        :return: True is matched => False if not
        """
        if self.hash_password(password=password) == self.password:
            return True
        return False

    def __repr__(self):
        return "<User {}>".format(self.username)
