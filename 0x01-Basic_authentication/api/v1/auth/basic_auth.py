#!/usr/bin/env python3
"""This module contains BasicAuth class"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Handles the Baisc Auth method to authenticate users"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """

        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split()[1]
