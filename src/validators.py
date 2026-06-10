"""
Input validation module for Calculator application.

This module provides validation functions for user input. All validators return
(bool, str) tuples where the bool indicates validity and the str contains an
error message if invalid (empty string if valid).

Functions:
    validate_numeric_input: Validates that input can be converted to float
    validate_menu_choice: Validates menu selection is in valid range
    validate_non_negative: Validates that a number is non-negative
"""

from typing import Tuple

# Error message constants
ERROR_INVALID_NUMBER = "Invalid number entered. Please enter a numeric value."
ERROR_EMPTY_INPUT = "Input cannot be empty. Please enter a value."
ERROR_INVALID_MENU = "Invalid menu choice. Please select a number from 0-8."
ERROR_NEGATIVE_VALUE = "Value must be non-negative."


def validate_numeric_input(user_input: str) -> Tuple[bool, str]:
    """
    Validate that user input is a valid number.

    Args:
        user_input: Raw string input from user

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if input is valid number, False otherwise
        - error_message: Empty string if valid, error description if invalid

    Examples:
        >>> validate_numeric_input("42.5")
        (True, "")
        >>> validate_numeric_input("-10")
        (True, "")
        >>> validate_numeric_input("abc")
        (False, "Invalid number entered. Please enter a numeric value.")
        >>> validate_numeric_input("")
        (False, "Invalid number entered. Please enter a numeric value.")
    """
    if not user_input or user_input.strip() == "":
        return (False, ERROR_INVALID_NUMBER)

    try:
        float(user_input)
        return (True, "")
    except ValueError:
        return (False, ERROR_INVALID_NUMBER)


def validate_menu_choice(user_input: str) -> Tuple[bool, str]:
    """
    Validate that user input is a valid menu choice (0-8).

    Args:
        user_input: Raw string input from user

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if input is valid menu choice, False otherwise
        - error_message: Empty string if valid, error description if invalid

    Examples:
        >>> validate_menu_choice("1")
        (True, "")
        >>> validate_menu_choice("8")
        (True, "")
        >>> validate_menu_choice("0")
        (True, "")
        >>> validate_menu_choice("9")
        (False, "Invalid menu choice. Please select a number from 0-8.")
        >>> validate_menu_choice("abc")
        (False, "Invalid menu choice. Please select a number from 0-8.")
    """
    try:
        choice = int(user_input)
        if 0 <= choice <= 8:
            return (True, "")
        else:
            return (False, ERROR_INVALID_MENU)
    except ValueError:
        return (False, ERROR_INVALID_MENU)


def validate_non_negative(number: float) -> Tuple[bool, str]:
    """
    Validate that a number is non-negative (>= 0).

    Args:
        number: The number to validate

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if number >= 0, False otherwise
        - error_message: Empty string if valid, error description if invalid

    Examples:
        >>> validate_non_negative(5.0)
        (True, "")
        >>> validate_non_negative(0.0)
        (True, "")
        >>> validate_non_negative(-5.0)
        (False, "Value must be non-negative.")
    """
    if number >= 0:
        return (True, "")
    else:
        return (False, ERROR_NEGATIVE_VALUE)

