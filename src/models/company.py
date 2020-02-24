from sqlalchemy import Column, Integer, String

from src.database import DbEngine


class Company(DbEngine.BASE):
    """
    This is a class for managing the Company model for the database.
    """
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __init__(self, name: str, email: str):
        """
        The constructor for the Company class.

        :param name: (str) the name of the company
        :param email: (str) the email address for the company
        """
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Company {}>".format(self.name)
