#!/usr/bin/env python3
"""This module contains Auth class"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Represents the auth process"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns whether the path is protected or not"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization Header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current authenticated user"""
