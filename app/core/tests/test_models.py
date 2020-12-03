from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test creating a new user with an email
        :return: new user
        """
        email = 'test@mail.com'
        passwd = '1234qwer'
        user = get_user_model().objects.create_user(
            email=email,
            password=passwd
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(passwd))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@MAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalis_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

