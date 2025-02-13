#!/usr/bin/env python3
"""
Module for filtering sensitive personal data from log messages.
"""
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection
from datetime import datetime
import bcrypt

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data' with specific settings.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger('user_data')

    logger.setLevel(logging.INFO)

    logger.propagate = False

    stream_handler = logging.StreamHandler()

    sensitive_fields = PII_FIELDS

    formatter = RedactingFormatter(fields=sensitive_fields)

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return


def get_db() -> connection.MySQLConnection:
    """
    Returns a MySQL database connection using credentials
    """
    db_config = {
        "user": os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        "password": os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        "host": os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        "database": os.getenv("PERSONAL_DATA_DB_NAME")
    }

    return mysql.connector.connect(**db_config)


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def main():
    """Main function to retrieve and log user data DB securely."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for f, r in zip(field_names, row))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
