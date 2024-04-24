#!/usr/bin/env python3
"""
Hash password module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    define _hash_password method that takes
    a password string args & return bytes.
    """
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    _hash_password = bcrypt.hashpw(password_bytes, salt)

    return _hash_password
