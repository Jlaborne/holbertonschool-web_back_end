#!/usr/bin/env python3
"""
Module for filtering sensitive personal data from log messages.
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with specific fields to redact.

        Args:
            fields (List[str]): List of fields to redact in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log messages, redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: The formatted log message with redacted fields.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replaces field values in a log message with a redacted string.

    Args:
        fields (List[str]): List of fields whose values should be obfuscated.
        redaction (str): The string to replace field values with.
        message (str): The log message.
        separator (str): The character separating fields in the message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = (f'({"|".join(map(re.escape, fields))})=[^ {separator}]*')
    return re.sub(pattern, lambda match: f'{match.group(1)}={redaction}',
                  message)
