from sqlalchemy import Column, Integer, String

from database.engine import Base


class Company(Base):
    """
    This is a class for managing the Company model for the database.
    """
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<Company {}>".format(self.name)
