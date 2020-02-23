from unittest import main, TestCase
from mock import patch

from src.database import DbEngine


class TestDbEngine(TestCase):

    @patch("config.GlobalParams")
    @patch("sqlalchemy.ext.declarative.declarative_base")
    @patch("src.database.sessionmaker")
    @patch("src.database.create_engine")
    def test___int__(self, mock_create_engine, mock_session, mock_declarative_base, mock_params):
        test = DbEngine()
        self.assertEqual(mock_create_engine.return_value, test.engine)
        self.assertEqual(mock_session.return_value.return_value, test.session)

        mock_session.assert_called_once_with(bind=mock_create_engine.return_value)
        mock_session.return_value.assert_called_once_with()


if __name__ == '__main__':
    main()
