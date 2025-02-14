#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from typing import List, TypeVar
from flask import request

User = TypeVar('User')


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Currently returns False for all paths; to be implemented later.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the Flask request object.
        Currently returns None; to be implemented later.
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Retrieves the current user based on the request.
        Currently returns None; to be implemented later.
        """
        return None
