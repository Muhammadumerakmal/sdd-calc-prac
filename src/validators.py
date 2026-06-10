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
