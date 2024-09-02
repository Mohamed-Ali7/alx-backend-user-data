#!/usr/bin/env python3
"""This module contains BasicAuth class"""

import binascii
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Rreturns the decoded value of a Base64
        string base64_authorization_header:
        """

        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            decoded_header = base64.b64decode(base64_authorization_header,
                                              validate=True)
            return decoded_header.decode("utf-8")
        except binascii.Error:
            return None
