#!/usr/bin/env python3
"""Authentication service module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hashed bytes."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user if they do not already exist."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode("utf-8")
            match = bcrypt.checkpw(pw_bytes, user.hashed_password)
            return match
        except NoResultFound:
            return False
