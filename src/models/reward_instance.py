from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.database import DbEngine


class RewardInstance(DbEngine.BASE):
    """
    This is a class for managing the RewardInstance model for the database.
    """
    __tablename__ = "rewardinstances"

    id = Column(Integer, primary_key=True)
    unique_id = Column(String(120), unique=True)
    title = Column(String(120))
    redeemed = Column(DateTime, nullable=True)

    reward = relationship("Reward")
    reward_id = Column(Integer, ForeignKey("rewards.id"), nullable=False)
    user = relationship("User")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return "<RewardInstance {}>".format(self.title)
