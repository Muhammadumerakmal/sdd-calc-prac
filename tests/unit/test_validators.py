"""
Unit tests for input validation functions.

Tests all validators in src/validators.py following the Red-Green-Refactor TDD approach.
All validators return (bool, str) tuples: (is_valid, error_message).
"""

import pytest
from src.validators import validate_numeric_input, validate_menu_choice, validate_non_negative


class TestValidateNumericInput:
    """Test cases for validate_numeric_input function."""

    def test_validate_numeric_input_valid_integer(self):
        """Test validation with valid integer strings."""
        is_valid, error = validate_numeric_input("42")
        assert is_valid is True
        assert error == ""

        is_valid, error = validate_numeric_input("100")
        assert is_valid is True
        assert error == ""

    def test_valid_decimal(self):
        """Test validation with valid decimal strings."""
        is_valid, error = validate_numeric_input("3.14")
        assert is_valid is True
        assert error == ""

        is_valid, error = validate_numeric_input("0.5")
        assert is_valid is True
        assert error == ""

    def test_valid_negative(self):
        """Test validation with valid negative numbers."""
        is_valid, error = validate_numeric_input("-10")
        assert is_valid is True
        assert error == ""

        is_valid, error = validate_numeric_input("-3.14")
        assert is_valid is True
        assert error == ""

    def test_validate_numeric_input_invalid_letters(self):
        """Test validation rejects letters."""
        is_valid, error = validate_numeric_input("abc")
        assert is_valid is False
        assert "Invalid number" in error

        is_valid, error = validate_numeric_input("12abc")
        assert is_valid is False
        assert "Invalid number" in error

    def test_invalid_empty(self):
        """Test validation rejects empty input."""
        is_valid, error = validate_numeric_input("")
        assert is_valid is False
        assert "empty" in error.lower() or "Invalid number" in error

    def test_invalid_special_chars(self):
        """Test validation rejects invalid special characters."""
        is_valid, error = validate_numeric_input("12@34")
        assert is_valid is False
        assert "Invalid number" in error

        is_valid, error = validate_numeric_input("$100")
        assert is_valid is False
        assert "Invalid number" in error


class TestValidateMenuChoice:
    """Test cases for validate_menu_choice function."""

    def test_validate_menu_choice_valid_range(self):
        """Test validation with valid menu choices (0-8)."""
        for choice in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
            is_valid, error = validate_menu_choice(choice)
            assert is_valid is True
            assert error == ""

    def test_invalid_out_of_range(self):
        """Test validation rejects out of range choices."""
        is_valid, error = validate_menu_choice("9")
        assert is_valid is False
        assert "Invalid menu choice" in error or "0-8" in error

        is_valid, error = validate_menu_choice("-1")
        assert is_valid is False
        assert "Invalid menu choice" in error or "0-8" in error

        is_valid, error = validate_menu_choice("100")
        assert is_valid is False
        assert "Invalid menu choice" in error or "0-8" in error

    def test_invalid_non_numeric(self):
        """Test validation rejects non-numeric input."""
        is_valid, error = validate_menu_choice("abc")
        assert is_valid is False
        assert "Invalid menu choice" in error

        is_valid, error = validate_menu_choice("")
        assert is_valid is False
        assert "Invalid menu choice" in error


class TestValidateNonNegative:
    """Test cases for validate_non_negative function."""

    def test_validate_non_negative_valid(self):
        """Test validation with non-negative numbers."""
        is_valid, error = validate_non_negative(0.0)
        assert is_valid is True
        assert error == ""

        is_valid, error = validate_non_negative(5.0)
        assert is_valid is True
        assert error == ""

        is_valid, error = validate_non_negative(100.5)
        assert is_valid is True
        assert error == ""

    def test_negative_rejected(self):
        """Test validation rejects negative numbers."""
        is_valid, error = validate_non_negative(-5.0)
        assert is_valid is False
        assert "non-negative" in error.lower() or "negative" in error.lower()

        is_valid, error = validate_non_negative(-0.1)
        assert is_valid is False
        assert "non-negative" in error.lower() or "negative" in error.lower()
