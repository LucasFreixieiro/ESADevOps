"""Tests
"""
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.

class UserTestCase(TestCase):
    """Test cases for user

    Args:
        TestCase (_type_): _description_
    """
    def test_user(self):
        """Verify if User created have the same password and username from start
        """
        username = 'shetu'
        password = 'hello'
        user = User(username=username)
        user.set_password(password)
        user.save()
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
