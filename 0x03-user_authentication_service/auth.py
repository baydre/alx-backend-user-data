#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from user import User
from typing import Optional


def _hash_password(password: str) -> bytes:
    """
    define _hash_password method that takes
    a password string args & return bytes.
    """
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    _hash_password = bcrypt.hashpw(password_bytes, salt)

    return _hash_password


def _generate_uuid() -> str:
    """
    generates UUIDs in str
    representation.
    """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """
        implements login function to
        respond to the POST /sessions route.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        implements get_user_from_session_id method
        takes single string args & returns the User or None.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user

    def destroy_session(self, user_id: str) -> None:
        """
        implements destroy_session
        and returns None.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        implement get_reset_password_token
        and returns a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token
