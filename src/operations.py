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



def power(base: float, exponent: float) -> float:
    """
    Raise base to the power of exponent.

    Args:
        base: The base number
        exponent: The exponent

    Returns:
        base raised to the power of exponent (base ^ exponent)

    Examples:
        >>> power(2.0, 8.0)
        256.0
        >>> power(10.0, 3.0)
        1000.0
        >>> power(5.0, 0.0)
        1.0
        >>> power(0.0, 0.0)
        1.0
    """
    return math.pow(base, exponent)


def square_root(number: float) -> float:
    """
    Calculate the square root of a number.

    Args:
        number: The number to find square root of

    Returns:
        Square root of the number

    Raises:
        ValueError: If number is negative

    Examples:
        >>> square_root(16.0)
        4.0
        >>> square_root(0.0)
        0.0
        >>> square_root(2.0)
        1.4142135623730951
        >>> square_root(-9.0)
        ValueError: Square root requires a non-negative number
    """
    if number < 0:
        raise ValueError("Square root requires a non-negative number")
    return math.sqrt(number)


def percentage(percent: float, of_value: float) -> float:
    """
    Calculate percentage of a value.

    Args:
        percent: The percentage (e.g., 20 for 20%)
        of_value: The value to calculate percentage of

    Returns:
        The calculated percentage value

    Examples:
        >>> percentage(20.0, 50.0)
        10.0
        >>> percentage(50.0, 100.0)
        50.0
        >>> percentage(100.0, 25.0)
        25.0
    """
    return (percent / 100.0) * of_value


def modulus(a: float, b: float) -> float:
    """
    Calculate remainder of division (a modulo b).

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Remainder of a / b

    Raises:
        ValueError: If b is zero

    Examples:
        >>> modulus(17.0, 5.0)
        2.0
        >>> modulus(10.0, 3.0)
        1.0
        >>> modulus(8.0, 4.0)
        0.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
