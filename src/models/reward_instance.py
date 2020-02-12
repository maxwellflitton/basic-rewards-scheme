from run import db


class RewardInstance(db.Model):
    """
    This is a class for managing the RewardInstance model for the database.
    """
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(120), unique=True)
    title = db.Column(db.String(120))
    redeemed = db.Column(db.DateTime, nullable=True)

    reward = db.relationship("Reward")
    reward_id = db.Column(db.Integer, db.ForeignKey("reward.id"), nullable=False)
    user = db.relationship("User")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return "<RewardInstance {}>".format(self.title)
