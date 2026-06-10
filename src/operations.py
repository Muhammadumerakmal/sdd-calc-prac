"""
Mathematical operations module for Calculator application.

This module provides pure mathematical functions for arithmetic and extended operations.
All functions are pure (no side effects) and raise ValueError for invalid inputs.

Functions:
    add: Addition of two numbers
    subtract: Subtraction of two numbers
    multiply: Multiplication of two numbers
    divide: Division with zero-check
    power: Exponentiation
    square_root: Square root with negative-check
    percentage: Percentage calculation
    modulus: Modulus/remainder operation
"""

import math
from typing import Union

Number = Union[int, float]


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add(2.0, 3.0)
        5.0
        >>> add(-5.0, 10.0)
        5.0
        >>> add(0.0, 0.0)
        0.0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        Difference (a - b)

    Examples:
        >>> subtract(10.0, 3.0)
        7.0
        >>> subtract(5.0, 10.0)
        -5.0
        >>> subtract(0.0, 0.0)
        0.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b

    Examples:
        >>> multiply(6.0, 7.0)
        42.0
        >>> multiply(-5.0, 3.0)
        -15.0
        >>> multiply(0.0, 100.0)
        0.0
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide first number by second number.

    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)

    Returns:
        Quotient (a / b)

    Raises:
        ValueError: If b is zero (division by zero)

    Examples:
        >>> divide(15.0, 3.0)
        5.0
        >>> divide(7.0, 2.0)
        3.5
        >>> divide(10.0, 0.0)
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

