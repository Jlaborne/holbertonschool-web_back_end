#!/usr/bin/env python3
"""
Module for filtering sensitive personal data from log messages.
"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Replaces field values in a log message with a redacted string.

    Args:
        fields (List[str]): List of field names whose values should be obfuscated.
        redaction (str): The string to replace field values with.
        message (str): The log message.
        separator (str): The character separating fields in the message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f'({"|".join(map(re.escape, fields))})=[^ {separator}]*'
    return re.sub(pattern, lambda match: f'{match.group(1)}={redaction}', message)
