from run import app_instance as app


class Reward(app.db.Model):
    """
    This is a class for managing the Reward model for the database.
    """
    __table_args__ = {'extend_existing': True}

    id = app.db.Column(app.db.Integer, primary_key=True)
    unique_id = app.db.Column(app.db.String(120), unique=True)
    title = app.db.Column(app.db.String(120))
    active_from = app.db.Column(app.db.DateTime, nullable=False)
    active_to = app.db.Column(app.db.DateTime, nullable=False)

    company = app.db.relationship("Company")
    company_id = app.db.Column(app.db.Integer, app.db.ForeignKey("company.id"), nullable=False)

    def __repr__(self):
        return "<Reward {}>".format(self.title)
