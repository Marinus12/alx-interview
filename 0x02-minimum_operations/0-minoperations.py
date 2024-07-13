#!/usr/bin/python3
"""Calculates the fewest number of operations needed to result in exactly
   n 'H' characters using only Copy All and Paste operations.
   """

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find all factors of n
    while n > 1:
        while n % divisor == 0:
            # Add the divisor to operations count
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
