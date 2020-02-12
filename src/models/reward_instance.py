from run import app_instance as app


class RewardInstance(app.db.Model):
    """
    This is a class for managing the RewardInstance model for the database.
    """
    __table_args__ = {'extend_existing': True}

    id = app.db.Column(app.db.Integer, primary_key=True)
    unique_id = app.db.Column(app.db.String(120), unique=True)
    title = app.db.Column(app.db.String(120))
    redeemed = app.db.Column(app.db.DateTime, nullable=True)

    reward = app.db.relationship("Reward")
    reward_id = app.db.Column(app.db.Integer, app.db.ForeignKey("reward.id"), nullable=False)
    user = app.db.relationship("User")
    user_id = app.db.Column(app.db.Integer, app.db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return "<RewardInstance {}>".format(self.title)
