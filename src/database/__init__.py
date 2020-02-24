from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import GlobalParams
params = GlobalParams()


class DbEngine:
    """
    This is an class for managing the connection and sessions to the database.

    Attributes:
        engine (sqlalchemy.create_engine.return_value): connection to DB
        session (sqlalchemy.orm.sessionmaker.return_value): manages sessions with database
    """
    BASE = declarative_base()

    def __init__(self):
        """
        The constructor for the DbEngine class.
        """
        self.engine = create_engine(params.get("DB_URL"), echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        """
        Creates tables for the database.

        :return: None
        """
        from src.models.user import User
        from src.models.reward import Reward
        from src.models.company import Company
        from src.models.reward_instance import RewardInstance
        User.__table__.create(bind=self.engine)
        Company.__table__.create(bind=self.engine)
        Reward.__table__.create(bind=self.engine)
        RewardInstance.__table__.create(bind=self.engine)
