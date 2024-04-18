#!/usr/bin/env python3
"""
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
        # For now, return false (no authentication)
        return False

    def authorization_header(self, request=None) -> str:
        """"""
        # For now, return None (no authorization header)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        # For now, return None (no current user)
        return None
