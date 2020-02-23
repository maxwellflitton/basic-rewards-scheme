# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
#
# from database.engine import Base
#
#
# class Reward(Base):
#     """
#     This is a class for managing the Reward model for the database.
#     """
#     __tablename__ = "rewards"
#
#     id = Column(Integer, primary_key=True)
#     unique_id = Column(String(120), unique=True)
#     title = Column(String(120))
#     active_from = Column(DateTime, nullable=False)
#     active_to = Column(DateTime, nullable=False)
#
#     company = relationship("Company")
#     company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
#
#     def __repr__(self):
#         return "<Reward {}>".format(self.title)
