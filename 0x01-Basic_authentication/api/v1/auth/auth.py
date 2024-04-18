#!/usr/bin/env python3
"""
Auth class: manages the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Determines whether authentication is required for a given path.

        Args:
            path (str): The requested path.
            excluded_paths (List[str]): List of paths that are exempt
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is required for a given path.

        Args:
            path (str): The requested path.
            excluded_paths (List[str]): List of paths that are exempt
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        # check if path is None or excluded_paths is None/empty
        if path is None or not excluded_paths:
            return True
        elif len(excluded_paths) == 0:
            return True

        # normalise the path by removing trailing slashes
        normalized_path = path.rstrip('/')
        for x in excluded_paths:
            stripped = x.rstrip('/')
            if normalized_path == stripped:
                return False
            if x[-1] == "*":
                if normalized_path.startswith(x[:-1]):
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from
        the Flask request.

        Args:
            request: The Flask request object (optional).

        Returns:
            str: The authorization header value
            (or None if not present).
        """
        # For now, return None (no authorization header)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves information about the current authenticated user.

        Args:
            request: The Flask request object (optional).

        Returns:
            TypeVar('User'): Information about the current user
            (or None if not authenticated).
        """
        # For now, return None (no current user)
        return None
