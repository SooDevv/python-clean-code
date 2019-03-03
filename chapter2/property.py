import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"It is not valid email. {new_email} can't be used")
        self._email = new_email


if __name__ == '__main__':
    u1 = User('soojung')
    u1.email = 'soojung.dev@github.io'
    print(u1.email)