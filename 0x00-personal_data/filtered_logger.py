#!/usr/bin/env python3
"""
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    """
    # creates a regex pattern for the specified fields.
    pattern = '|'.join(re.escape(field) for field in fields)

    # replace occurrences of field values with the redaction
    obfuscated_message = re.sub(pattern, redaction, message)

    return obfuscated_message
