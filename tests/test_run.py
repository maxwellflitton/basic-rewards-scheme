from unittest import TestCase, main
from mock import patch

from run import create_app


class TestCreateApp(TestCase):

    @patch("run.Flask")
    def test_create_app(self, mock_app):
        test = create_app()
        self.assertEqual(mock_app.return_value, test)


if __name__ == "__main__":
    main()
