#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            # Determine the number of bytes
            while mask & num:
                number_of_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if number_of_bytes == 0:
                continue

            # Invalid scenarios
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # Check if the most significant bits are '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrease the number of bytes remaining
        number_of_bytes -= 1

    return number_of_bytes == 0
