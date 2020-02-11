from unittest import TestCase, main
from mock import patch, MagicMock

from singleton import Singleton


class TestCreateApp(TestCase):

    def tearDown(self) -> None:
        Singleton._instances = {}

    @patch("flask.Flask")
    @patch("flask_sqlalchemy.SQLAlchemy")
    def test___init__(self, mock_db, mock_app):
        from run import AppEngine
        test = AppEngine()
        self.assertEqual(mock_app.return_value, test.app)
        self.assertEqual(mock_db.return_value, test.db)

    @patch("flask.Flask")
    @patch("flask_sqlalchemy.SQLAlchemy")
    @patch("models.user.User")
    def test_import_models(self, mock_user, mock_db, mock_app):
        from run import AppEngine
        test = AppEngine()
        test.db = MagicMock()


if __name__ == "__main__":
    main()
