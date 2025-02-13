#!/usr/bin/env python3
"""
Hashing and verifying passwords using bcryp
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password with a new salt"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if the provided password matches the hashed password """
    return bcrypt.checkpw(password.encode(), hashed_password)
