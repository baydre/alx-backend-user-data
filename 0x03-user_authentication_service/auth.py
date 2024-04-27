#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


def _hash_password(password: str) -> bytes:
    """
    define _hash_password method that takes
    a password string args & return bytes.
    """
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    _hash_password = bcrypt.hashpw(password_bytes, salt)

    return _hash_password


class Auth:
    """Auth class to interact with authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        implements the Auth.register_user using
        email & password string args and return
        a User object.
        """
        # Check if user already exists
        try:
            existing_user = self._db.find_user_by(email=email)
        except NoResultFound:
            # Hash the password
            password = _hash_password(password)

            # Save new user to the database
            new_user = self._db.add_user(email, password)
            return new_user
        else:
            raise ValueError(f"User {email} already exists.")


    def valid_login(self, email: str, password: str) -> bool:
        """
        implements Auth.valid_login method and
        returns boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode('utf-8'),
                    hashed_password=user.hashed_password)
