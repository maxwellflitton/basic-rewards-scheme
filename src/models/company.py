from run import app_instance as app


class Company(app.db.Model):
    """
    This is a class for managing the Company model for the database.
    """
    __table_args__ = {'extend_existing': True}

    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(120), unique=True, nullable=False)
    email = app.db.Column(app.db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<Company {}>".format(self.name)
