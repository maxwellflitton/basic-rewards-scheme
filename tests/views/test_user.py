from unittest import main, TestCase
from mock import patch, MagicMock

from views.user import user, login, register


class TestUserViews(TestCase):

    def test_user(self):
        self.assertEqual("basic user view", user())

    @patch("views.user.login_user")
    @patch("views.user.render_template")
    @patch("views.user.redirect")
    @patch("views.user.flash")
    @patch("views.user.url_for")
    @patch("views.user.model_factory")
    @patch("views.user.LoginForm")
    def test_login(self, mock_login, mock_model_factory, mock_url_for, mock_flash, mock_redirect, mock_render_template,
                   mock_login_user):
        mock_login.return_value.validate_on_submit.return_value = False
        out_come = login()

        self.assertEqual(mock_render_template.return_value, out_come)
        mock_render_template.assert_called_once_with("login.html", title="login_page", form=mock_login.return_value)

        mock_render_template.reset_mock()

        mock_login.return_value.validate_on_submit.return_value = True

        mock_model_factory.return_value.query.filter_by.return_value.first.return_value = None

        out_come = login()

        mock_model_factory.assert_called_once_with(model="user")
        mock_flash.assert_called_once_with('Invalid username or password')
        mock_redirect.assert_called_once_with(mock_url_for.return_value)
        mock_url_for.assert_called_once_with("login")

        self.assertEqual(mock_redirect.return_value, out_come)

        mock_model_factory.reset_mock()
        mock_redirect.reset_mock()
        mock_url_for.reset_mock()

        mock_model_factory.return_value.query.filter_by.return_value.first.return_value = MagicMock()

        out_come = login()
        mock_model_factory.assert_called_once_with(model="user")
        mock_flash.assert_called_once_with('Invalid username or password')

        mock_login_user.assert_called_once_with(
            mock_model_factory.return_value.query.filter_by.return_value.first.return_value,
            remember=mock_login.return_value.remember_me.data
        )
        self.assertEqual(mock_redirect.return_value, out_come)
        mock_redirect.assert_called_once_with(mock_url_for.return_value)
        mock_url_for.assert_called_once_with("index")

    @patch("views.user.url_for")
    @patch("views.user.render_template")
    @patch("views.user.redirect")
    @patch("views.user.flash")
    @patch("views.user.model_factory")
    @patch("views.user.RegistrationForm")
    def test_register(self, mock_reg_form, mock_model_factory, mock_flash, mock_redirect, mock_render_template,
                      mock_url_for):
        mock_reg_form.return_value.validate_on_submit.return_value = False
        out_come = register()
        mock_render_template.assert_called_once_with("register.html", title="register_page",
                                                     form=mock_reg_form.return_value)
        self.assertEqual(mock_render_template.return_value, out_come)

        mock_reg_form.return_value.validate_on_submit.return_value = MagicMock()

        out_come = register()

        self.assertEqual(mock_redirect.return_value, out_come)
        mock_model_factory.assert_called_once_with(model="user")
        mock_model_factory.return_value.assert_called_once_with(username=mock_reg_form.return_value.username.data,
                                                                email=mock_reg_form.return_value.email.data,
                                                                password=mock_reg_form.return_value.password.data)
        mock_model_factory.return_value.return_value.save_instance.assert_called_once_with()
        mock_flash.assert_called_once_with('Congratulations, you are now a registered user!')
        mock_redirect.assert_called_once_with(mock_url_for.return_value)
        mock_url_for.assert_called_once_with('login')


if __name__ == '__main__':
    main()
