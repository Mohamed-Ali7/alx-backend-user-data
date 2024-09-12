#!/usr/bin/env python3

"""This module contains _hash_password() method"""

import bcrypt


def _hash_password(password: str):
    """Returns salted hash of the input password as bytes"""

    pwd_salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), pwd_salt)

    return hashed_password
