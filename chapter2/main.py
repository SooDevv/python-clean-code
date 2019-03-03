"""Test script"""

import unittest
from property import User, is_valid_email


class TestProperty(unittest.TestCase):
    def test_is_valid_email(self):
        data = ("soodevv@github.com", "soojung.dev@gmail.com")
        for email in data:
            self.assertTrue(is_valid_email(email))

    def test_invalid_email(self):
            self.assertFalse(is_valid_email("invalid"))

    def test_user_valid_email(self):
        user = User("soojung")
        user.email = "soojung@gmail.com"
        self.assertEqual(user.email, "soojung@gmail.com")

    def test_user_invalid_domain(self):
        user = User("username")
        with self.assertRaisesRegex(
            ValueError, "Can't set .* not a valid email"
        ):
            user.email = "something"


if __name__ == "__main__":
    unittest.main()