from run import db


class Reward(db.Model):
    """
    This is a class for managing the Reward model for the database.
    """
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(120), unique=True)
    title = db.Column(db.String(120))
    active_from = db.Column(db.DateTime, nullable=False)
    active_to = db.Column(db.DateTime, nullable=False)

    company = db.relationship("Company")
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)

    def __repr__(self):
        return "<Reward {}>".format(self.title)
