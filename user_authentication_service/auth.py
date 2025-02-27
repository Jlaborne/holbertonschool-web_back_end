#!/usr/bin/env python3
"""Authentication service module"""

import bcrypt
from db import DB
from user import Use


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hashed bytes."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
