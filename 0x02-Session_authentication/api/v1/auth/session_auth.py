#!/usr/bin/env python3
"""This module contains SessionAuth class"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Handles the Session Auth method to authenticate users"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""

        if not user_id or type(user_id) is not str:
            return None

        session_id = uuid.uuid4()

        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id
