#!/usr/bin/env python3

"""This module contains _hash_password() method"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Returns salted hash of the input password as bytes"""

    pwd_salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), pwd_salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            raise ValueError("User {} already exists".format(email))
