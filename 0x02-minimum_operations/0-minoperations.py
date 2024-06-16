#!/usr/bin/python3
"""MINIMUM OPERATIONS"""


def minOperations(n):
    """Calculates the minimum operations"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
